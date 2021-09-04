# 문제: https://programmers.co.kr/learn/courses/30/lessons/72413

# --- 첫 풀이 ---

from heapq import heappop, heappush

def dijkstra(graph, start):
    n = len(graph)
    INF = float("inf")
    cost = [INF] * (n+1)
    queue = []
    heappush(queue, (0, start))
    cost[start] = 0
    
    while queue:
        c, cur_node = heappop(queue)
                
        if cost[cur_node] < c:
            continue
        
        for next_node, dist in graph[cur_node]:        
            nc = c + dist
            
            if cost[next_node] <= nc:
                continue
            
            cost[next_node] = nc
            heappush(queue, (nc, next_node))
    
def solution(n, s, a, b, fares):
    answer = 0
    return answer
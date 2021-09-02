from heapq import heappop, heappush

# def get_graph(n, roads):
#     graph = [[] for _ in range(n + 1)]
    
#     for r in roads:
#         graph[r[0]].append((r[1], r[2]))
    
#     return graph

# def get_new_graph(graph, trap):
#     trap_node = list(graph[trap])
    
#     for i, nodes in enumerate(graph):
#         for node in nodes:
#             if node[0] == trap:
#                 graph[trap].append((i, node[1]))
#                 nodes.remove(node)
    
#     for t in trap_node:
#         graph[trap].remove(t)
#         graph[t[0]].append((trap, t[1]))
    
#     return graph

def get_graph(n, roads):
    INF = float("inf")
    graph = [[INF] * (n+1) for _ in range(n + 1)]
    
    for r in roads:
        graph[r[0]][r[1]] = min(graph[r[0]][r[1]], r[2])
    
    return graph

def get_new_graph(graph, trap):
    for i in range(len(graph)):
        graph[trap][i], graph[i][trap] = graph[i][trap], graph[trap][i]
        
    return graph

def dijkstra(start, end, graph, traps, visited):
    INF = float("inf")
    queue = []
    heappush(queue, (0, start))
    visited[start] = True
    
    while queue:
        total_time, node = heappop(queue)
        
        if node == end:
            return total_time

        if node in traps:
            graph = get_new_graph(graph, node)
        
        for next_node, time in enumerate(graph[node]):
            if time == INF:
                continue
            
            if visited[next_node]:
                continue
            
            heappush(queue, (total_time + time, next_node))
            
            if next_node not in traps:
                visited[next_node] = True

        
def solution(n, start, end, roads, traps):
    graph = get_graph(n, roads)
    visited = [False] * (n+1)
    
    return dijkstra(start, end, graph, traps, visited)

# --- 모범 답안 ---
# 문제: https://programmers.co.kr/learn/courses/30/lessons/81304

from collections import defaultdict
from heapq import heappop, heappush

def get_graph(roads):
    graph = defaultdict(list)
    
    # 초기상태의 상황 입력, 3번째 인자는 정방향이면 True, 역방향이면 False
    for a, b, cost in roads:
        graph[a].append((b, cost, True))
        graph[b].append((a, cost, False))
    
    return graph

def solution(n, start, end, roads, traps):
    INF = float("inf")
    graph = get_graph(roads)
    trap_dict = dict()  # trap_dict는 traps의 값들을 0부터 순차적으로 넣기 위해, 궁극적으로는 비트마스킹을 이용하기 위해 변환에 필요한 딕셔너리
    
    for idx, trap in enumerate(sorted(traps)):
        trap_dict[trap] = idx
        
    times = [[INF] * (n+1) for _ in range(2 ** len(traps))] # times[trap_state][x] = trap_state인 상태에서, start에서 출발해서 x까지 가는데 걸리는 최소 시간

    def dijactra(start):
        times[0][start] = 0
        queue = []
        heappush(queue, (0, start, 0))
        
        while queue:
            cur_time, cur_node, trap_state = heappop(queue)
            
            if times[trap_state][cur_node] < cur_time:
                continue
            
            if cur_node in traps:
                idx = trap_dict[cur_node]
                x = True if trap_state & (1 << idx) else False
            else:
                x = False

            """
            init_dir: 초기상태 방향 판단 (True / False)
            x: 현재 cur_node가 발동이 된 함정이라면 True 아니라면 False (함정이 아니면 False)
            y: 현재 adj_node가 발동이 된 함정이라면 True 아니라면 False (함정이 아니면 False)
            init_dir ^ (x^y): cur_node에서 adj_node로 갈 수 있다면 True 없다면 False

            init_dir  x      y          init_dir ^ (x^y)
            --------------------------------------------
            True     True    True   ->  True
            True     True    False  ->  False
            True     False   True   ->  False
            True     False   False  ->  True
   
            False    True    True   ->  False
            False    True    False  ->  True
            False    False   True   ->  True
            False    False   False  ->  False
            """
            
            for adj_node, time, init_dir in graph.get(cur_node):
                if adj_node in traps:
                    idx = trap_dict[adj_node]
                    y = True if trap_state & (1 << idx) else False
                else:
                    y = False
                    
                if init_dir ^ (x^y):  # cur_node에서 adj_node로 갈 수 있다면
                    if adj_node in traps:
                        next_trap_state = trap_state ^ (1 << idx)
                        
                        if cur_time + time < times[next_trap_state][adj_node]:
                            times[next_trap_state][adj_node] = cur_time + time
                            heappush(queue, [cur_time + time, adj_node, next_trap_state])
                    else:
                        if cur_time + time < times[trap_state][adj_node]:
                            times[trap_state][adj_node] = cur_time + time
                            heappush(queue, [cur_time + time, adj_node, trap_state])

    # 다익스트라 알고리즘 실행
    dijactra(start)

    # 모든 trap의 상황에 따른 end노드까지의 값들 중 최솟값을 answer에 대입
    answer = INF
    
    for time in times:
        answer = min(answer, time[end])
            
    return answer
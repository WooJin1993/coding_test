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

from heapq import heappop, heappush
from collections import defaultdict

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
    
    # trap_dict는 traps의 값들을 0부터 순차적으로 넣기 위해, 궁극적으로는 비트마스킹을 이용하기 위해 변환에 필요한 딕셔너리
    trap_dict = dict()
    
    for idx, trap in enumerate(sorted(traps)):
        trap_dict[trap] = idx
        
    # distances[trap_state][x] = trap_state인 상태에서 x까지 가는데 걸리는 총 cost
    distances = [[INF] * (n+1) for _ in range(2 ** len(traps))]

    def dijactra(start, end):
        distances[0][start] = 0
        queue = []
        heappush(queue, (0, start, 0))
        
        while queue:
            cur_dis, cur_node, cur_trap = heappop(queue)
            
            if distances[cur_trap][cur_node] < cur_dis:
                continue
            
            if cur_node in traps:
                trap_idx = trap_dict[cur_node]
                x = True if cur_trap & (1 << trap_idx) >= 1 else False
            else:
                x = False

            """
            token: 초기상태 방향 판단 (True / False)
            x: cur_node에 따른 방향 (cur_node가 방향 바뀌는데 기여했으면 True 아니면 False)
            y: adj에 따른 방향 (adj가 방향 바뀌는데 기여했으면 True 아니면 False)
            token ^ (x ^ y): 초기 상황에 대해서 방향이 몇 번 틀어졌는지 계산해서 이동할 수 있는 간선인지 판단하는 식

            [token]  [x]     [y]        [result]
            True     True    True   ->  True
            True     True    False  ->  False
            True     False   True   ->  True
            True     False   False  ->  False
   
            False    True    True   ->  False
            False    True    False  ->  True
            False    False   True   ->  True
            False    False   False  ->  False
            """
            
            for adj, cost, token in graph.get(cur_node):
                if adj in traps:
                    you = trap_dict[adj]
                    y = True if cur_trap & (1 << you) >= 1 else False
                else:
                    y = False
                    
                if token ^ (x ^ y):  # 이동할 수 있는 경로라면
                    if adj in traps:
                        next_trap = cur_trap ^ (1 << you)
                        
                        if cur_dis + cost < distances[next_trap][adj]:
                            distances[next_trap][adj] = cur_dis + cost
                            heappush(queue, [cur_dis + cost, adj, next_trap])
                    else:
                        if cur_dis + cost < distances[cur_trap][adj]:
                            distances[cur_trap][adj] = cur_dis + cost
                            heappush(queue, [distances[cur_trap][adj], adj, cur_trap])

    # 다익스트라 알고리즘 실행
    dijactra(start, end)

    # 모든 trap의 상황에 따른 end노드까지의 값들 중 최솟값을 answer에 대입
    answer = INF
    
    for distance in distances:
        answer = min(answer, distance[end])
            
    return answer
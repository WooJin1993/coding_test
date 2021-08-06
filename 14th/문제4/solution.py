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
# 문제: https://www.acmicpc.net/problem/2021

from heapq import heappop, heappush
from sys import stdin

N, L = map(int, input().split())
INF = float("inf")
lines = []
stations = [[] for _ in range(N + 1)]
transfer = [INF] * (N+1)
visited = [False] * L

for i in range(L):
    line = list(map(int, stdin.readline().split()))[:-1]
    lines.append(line)
    
    for s in line:
        stations[s].append(i)

start, end = map(int, input().split())

def dijkstra():
    queue = []
    transfer[start] = 0
    heappush(queue, (-1, start))
    
    while queue:
        cnt, curr_s = heappop(queue)
        
        if transfer[curr_s] < cnt:
            continue
        
        for line in stations[curr_s]:
            if visited[line]:
                continue
            
            visited[line] = True
            
            for next_s in lines[line]:
                if next_s == end:
                    return cnt + 1
                
                if transfer[next_s] > cnt + 1:
                    transfer[next_s] = cnt + 1
                    heappush(queue, (cnt + 1, next_s))
                    
    return -1

print(dijkstra())
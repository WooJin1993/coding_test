# 문제: https://programmers.co.kr/learn/courses/30/lessons/72413

# --- 풀이 ---
# INF = sys.maxsize 하는 경우, 효율성 테스트 1개 실패
# 계산 시간은 INF 크기에도 영향을 받는다.

from itertools import product

def solution(n, s, a, b, fares):
    result = []
    INF = 1e12
    graph = [[INF] * (n+1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    for c, d, f in fares:
        graph[c][d] = graph[d][c] = f
    
    for k, i, j in product(range(1, n + 1), repeat=3):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for mid in range(1, n + 1):
        result.append(graph[s][mid] + graph[mid][a] + graph[mid][b])

    return min(result)
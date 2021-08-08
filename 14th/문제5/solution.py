# --- 첫 번째 풀이 ---
# 시험 당시의 풀이

from operator import itemgetter

def solution(k, num, links):
    result = []
    threshold = (sum(num) // k) + 1
    
    while k > 0:
        idx_list = []
        idx = links.index([-1, -1])
        links[idx] = [-1]
        idx_list.append(idx)
        group_sum = 0
        group_sum += num[idx]
        
        while sum(itemgetter(*idx_list)(num)) < threshold:
            # 자식
            for link in links:
                node = [l for l in link if l not in idx_list and l != -1] 
                if not node:
                    if group_sum + num[node[0]] < threshold:
                        idx_list.append(node[0])
                        group_sum += num[node[0]]
                    else:
                        result.append(group_sum)
                        k -= 1
                        break
            # 부모
            for i, link in enumerate(links):
                if idx_list[-1] in link:
                    idx_list.append(i)
                    link[i][link[i].index(idx_list[-1])] = -1
                if sum(itemgetter(*idx_list)(num)) < threshold:
                    idx_list.append()
        
        for idx in idx_list:
            for link in links:
                if idx in link:
                    link[link.index(idx)] = -1
        
        k -= 1
        result.append(sum(itemgetter(*idx_list)(num)))
    
    return max(result)

# --- 두 번째 풀이 ---

from itertools import combinations
                
def get_graph_edges(links):
    n = len(links)
    graph = [[] for _ in range(n)]
    edges = []
    
    for i, link in enumerate(links):
        if link[0] != -1:
            graph[i].append(link[0])
            edges.append((i, link[0]))
        if link[1] != -1:
            graph[i].append(link[1])
            edges.append((i, link[1]))
    
    return graph, edges

def get_csum_list(num, graph):
    n = len(graph)
    csum_list = list(num)
    nodes = {i for i, g in enumerate(graph) if not g} # leaf_nodes
    levels = [0] * n
    level = 1
    
    for n in nodes:
        levels[n] = level
    
    while nodes:
        level += 1
        temp_nodes = set()
        
        for i, g in enumerate(graph):
            intersect = set(g) & nodes
            
            if not intersect:
                continue
            
            for j in intersect:
                csum_list[i] += csum_list[j]
                
            temp_nodes.add(i)
        
        nodes = temp_nodes
        
        for n in nodes:
            levels[n] = level
    
    return csum_list, levels
 
def solution(k, num, links):
    graph, edges  = get_graph_edges(links)
    csum_list, levels = get_csum_list(num, graph)
    result = []
    
    for i in range(len(edges)):
        edges[i] = (*edges[i], levels[edges[i][1]])
    
    for comb in combinations(edges, k - 1):
        comb = sorted(comb, key=lambda x: x[2], reverse=True)
        temp_csum = list(csum_list)
        
        for c in comb:
            temp_csum[c[0]] -= temp_csum[c[1]]
        
        result.append(max(temp_csum))
    
    return min(result)

# --- 세 번째 풀이 ---

def get_graph(links):
    graph = [[] for _ in range(len(links))]
    
    for i, link in enumerate(links):
        if link[0] != -1:
            graph[i].append(link[0])
        if link[1] != -1:
            graph[i].append(link[1])
    
    return graph

def parametric_search(num, graph, k, L):
    n = len(num)
    INF = float("inf")
    dp = [[INF, INF] for _ in range(n)]
    nodes = {i for i, g in enumerate(graph) if not g} # leaf_nodes
    
    for node in nodes:
        if num[node] > L:
            return False
        
        dp[node] = [1, num[node]]
    
    while nodes:
        temp_nodes = set()
        
        for i, g in enumerate(graph):
            intersect = set(g) & nodes
            
            if not intersect:
                continue
            
            if len(intersect) == 2:
                left, right = intersect
                
                if num[i] + dp[left][1] + dp[right][1] <= L:
                    dp[i][0] = dp[left][0] + dp[right][0] - 1
                    dp[i][1] = num[i] + dp[left][1] + dp[right][1]
                elif num[i] + dp[left][1] <= L or num[i] + dp[right][1] <= L:
                    dp[i][0] = dp[left][0] + dp[right][0]
                    dp[i][1] = num[i] + min(dp[left][1], dp[right][1])
                elif num[i] <= L:
                    dp[i][0] = dp[left][0] + dp[right][0] + 1
                    dp[i][1] = num[i]
                else:
                    return False
            else:
                child = intersect.pop()
                
                if num[i] + dp[child][1] <= L:
                    dp[i][0] = dp[child][0] - 1
                    dp[i][1] = num[i] + dp[child][1]
                elif num[i] + dp[child][1] <= L:
                    dp[i][0] = dp[child][0]
                    dp[i][1] = num[i] + dp[child][1]
                elif num[i] <= L:
                    dp[i][0] = dp[child][0] + 1
                    dp[i][1] = num[i]
                else:
                    return False
                
            temp_nodes.add(i)
        
        nodes = temp_nodes
    
    if max(dp, key=lambda x: x[0])[0] > k:
        return False
    else:
        return True  
    
def solution(k, num, links):
    graph = get_graph(links)
    L = sum(num) // k
    
    while True:
        if parametric_search(num, graph, k, L):
            return L
        else:
            L += 1
            

# --- 모범 답안 ---
import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)

def dfs(l, idx, num, dp, child):
    if idx == -1:
        return

    left = child[idx][0]
    right = child[idx][1]

    dfs(l, left, num, dp, child)
    dfs(l, right, num, dp, child)

    dp[idx][0] = dp[left][0] + dp[right][0]
    
    if num[idx] + dp[left][1] + dp[right][1] <= l:
        dp[idx][1] = num[idx] + dp[left][1] + dp[right][1]
    elif num[idx] + dp[left][1] <= l or num[idx] + dp[right][1] <= l:
        dp[idx][0] += 1
        dp[idx][1] = num[idx] + min(dp[left][1], dp[right][1])
    else:
        dp[idx][0] += 2
        dp[idx][1] = num[idx]
        
        if num[idx] > l:
            dp[idx][0] = 10000

    return dp[idx][0]

def solution(k, num, links):
    par = [-1 for _ in range(len(num))]
    
    for i, (left, right) in enumerate(links):
        if left != -1:
            par[left] = i
        if right != -1:
            par[right] = i

    root_idx = 0
    
    while par[root_idx] != -1:
        root_idx = par[root_idx]

    start = sum(num) // k
    end = sum(num)
    answer = end
    num += [0]
    
    while start <= end:
        mid = (start+end) // 2
        dp = [[0, 0] for _ in range(len(num))]
        
        if dfs(mid, root_idx, num, dp, links) < k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
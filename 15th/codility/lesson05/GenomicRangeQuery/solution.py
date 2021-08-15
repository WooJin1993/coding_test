# --- 풀이 1 ---
# 62점

def solution(S, P, Q):
    S_dict = {"A": 1, "C": 2, "G": 3, "T": 4}
    S_num = []
    
    for x in S:
        S_num.append(S_dict[x])
    
    result = []
    
    for x, y in zip(P, Q):
        result.append(min(S_num[x:y + 1]))
    
    return result

# --- 풀이 2 ---

def init(array, tree, node, start, end):
    if start == end:
        tree[node - 1] = start
    else:
        left, right = 2 * node, 2*node + 1
        
        init(array, tree, left, start, (start+end) // 2)
        init(array, tree, right, (start+end)//2 + 1, end)
        
        if array[tree[2*node - 1]] < array[tree[2 * node]]:
            tree[node - 1] = tree[2*node - 1]
        else:
            tree[node - 1] = tree[2 * node]

def solution(S, P, Q):
    S_dict = {"A": 1, "C": 2, "G": 3, "T": 4}
    S_num = [S_dict[x] for x in S]
    tree = [0] * (2*len(S) - 1)
    
    init(S_num, tree, 0, 0, len(S_num) - 1)
    
    print(tree)

    
    
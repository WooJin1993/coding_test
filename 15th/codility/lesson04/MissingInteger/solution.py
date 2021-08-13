# --- 풀이 1 ---
# 효율성 1개 실패

def solution(A):
    A = {x for x in A if x > 0}
    
    try:
        max_A = max(A)
    except ValueError:
        max_A = 0
        
    return min(set(range(1, max_A + 2)) - A)


# --- 풀이 2 ---

def solution(A):
    max_A = max(A)
    
    if max_A <= 0:
        return 1
    
    return min(set(range(1, max_A + 2)) - set(A))
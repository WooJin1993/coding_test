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

def solution(S, P, Q):
    S_dict = [("A", 1), ("C", 2), ("G", 3), ("T", 4)]
    result = []
    
    for x, y in zip(P, Q):
        query = S[x:y + 1]
        
        for key, value in S_dict:
            if key in query:
                result.append(value)
                break
    
    return result
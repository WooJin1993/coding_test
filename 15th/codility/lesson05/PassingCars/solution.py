# --- 풀이 1 ---
# 50점 (시간 초과로 -50점)

def solution(A):
    answer = 0
    
    for i in range(len(A)):
        if A[i] == 0:
            answer += sum(1 for j in range(i + 1, len(A)) if A[j] == 1)
    
    if answer > 1e9:
        return -1
    
    return answer

# --- 풀이 2 ---

def solution(A):
    answer = 0
    cum_sum = 0
    
    for x in reversed(A):
        if x == 1:
            cum_sum += 1
        else:
            answer += cum_sum
    
    if answer > 1e9:
        return -1
    
    return answer
            
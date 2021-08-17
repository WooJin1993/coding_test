# --- 풀이 1 ---
# 90점 (1개 실패)

from collections import deque

def solution(A):
    result = deque([(A[-2] + A[-1], 2)])
    
    for i in reversed(range(len(A) - 2)):
        cum_sum, length = result[0]
        cum_mean = (cum_sum+A[i]) / (length+1)
        
        if cum_mean <= (A[i]+A[i + 1]) / 2:
            result.appendleft((cum_sum+A[i], length+1))
        else:
            result.appendleft((A[i] + A[i + 1], 2))
    
    result = [r[0] / r[1] for r in result]

    return sorted(enumerate(result), key=lambda x: x[1])[0][0]

# --- 풀이 2 ---
# 참고: https://nukeguys.tistory.com/175

def solution(A):
    min_avg = (A[0]+A[1]) / 2
    min_idx = 0
    
    for i in range(2, len(A)):
        avg = (A[i - 2]+A[i - 1]+A[i]) / 3
        
        if avg < min_avg:
            min_avg = avg
            min_idx = i - 2
        
        avg = (A[i - 1]+A[i]) / 2
        
        if avg < min_avg:
            min_avg = avg
            min_idx = i - 1
    
    return min_idx
        
        
            
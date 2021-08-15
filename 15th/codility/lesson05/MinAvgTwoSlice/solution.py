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
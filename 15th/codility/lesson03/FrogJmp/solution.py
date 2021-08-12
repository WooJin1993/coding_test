def solution(A, K):
    K = K % len(A)
    
    if K == 0:
        return A
    
    return A[K - 1:] + A[:K - 1]
    
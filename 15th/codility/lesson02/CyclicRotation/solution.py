def solution(A, K):
    try:
        K %= len(A)
    except ZeroDivisionError:
        return []
    
    return A[len(A) - K:] + A[:len(A) - K]
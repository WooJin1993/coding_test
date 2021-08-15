def solution(A, B, K):
    q, r = divmod(A, K)
    
    if r:
        start = (q+1) * K
    else:
        start = A
    
    return len(range(start, B + 1, K))
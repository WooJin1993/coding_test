def solution(A):
    
    return (set(range(1, len(A) + 2)) - set(A)).pop()
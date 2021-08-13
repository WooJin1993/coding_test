from collections import Counter

def solution(A):
    A_counter = Counter(A)
    
    if max(A_counter.values()) >= 2:
        return 0
    
    A_keys = set(A_counter.keys())
    max_A = max(A_counter.keys())
    
    if len(A_keys) != max_A:
        return 0
    
    if A_keys - set(range(1, max_A + 1)):
        return 0
    
    return 1
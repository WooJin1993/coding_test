from collections import defaultdict

def solution(X, A):
    A_counter = defaultdict(int)
    
    for i, element in enumerate(A):
        A_counter[element] += 1
        
        if len(A_counter) == X:
           return i 

    return -1
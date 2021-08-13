from collections import defaultdict

def solution(N, A):
    A_counter = defaultdict(int)
    max_counter = 0
    
    for x in A:
        if x == N + 1:
            try:
                max_counter += max(A_counter.values())
            except ValueError:
                pass
            
            A_counter = defaultdict(int)
        else:
            A_counter[x] += 1
    
    result = [max_counter] * N
    
    for key, value in A_counter.items():
        result[key - 1] += value
    
    return result
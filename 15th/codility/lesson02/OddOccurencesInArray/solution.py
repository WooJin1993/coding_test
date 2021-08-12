from collections import Counter

def solution(A):
    A_counter = Counter(A)
    
    for key, value in A_counter.items():
        if value % 2 != 0:
            return key
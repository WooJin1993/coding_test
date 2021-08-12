from collections import Counter

def solution(A):
    A_counter = Counter(A)
    
    return A_counter.most_common()[-1][0]
def solution(N):
    N_bin = bin(N)[2:]
    answer = 0
    one_idx = -1
    
    for i, x in enumerate(N_bin):
        if x == "1":
            answer = max(answer, one_idx - i - 1)
            one_idx = i
    
    return answer
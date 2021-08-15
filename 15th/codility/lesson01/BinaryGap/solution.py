def solution(N):
    N_bin = bin(N)[2:]
    answer = 0
    temp_answer = 0
    
    for x in N_bin:
        if x == "1":
            answer = max(answer, temp_answer)
            temp_answer = 0
        else:
            temp_answer += 1
    
    return answer
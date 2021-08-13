def solution(A):
    cum_sums = []
    cum_sum = 0
    
    for x in A:
        cum_sum += x
        cum_sums.append(cum_sum)
    
    result = []
    max_cum_sum = cum_sums[-1]
    
    for i in range(1, len(A)):
        result.append(abs(max_cum_sum - 2*cum_sums[i - 1]))
    
    return min(result)
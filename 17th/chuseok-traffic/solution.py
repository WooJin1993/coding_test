# 문제: https://programmers.co.kr/learn/courses/30/lessons/17676

from bisect import bisect_left, bisect_right

def solution(lines):
    starts, ends = [], []
    
    for line in lines:
        S, T = line[11:].split()
        T = int(1000 * float(T.replace("s", "")))
        
        end = int(S[:2]) * 3600000 + int(S[3:5]) * 60000 + int(S[6:8]) * 1000 + int(S[9:])
        start = end - (T-1)
        
        starts.append(start)
        ends.append(end)
    
    starts.sort()
    ends.sort()
    result = []
    
    for start, end in zip(starts, ends):
        start_time = start
        end_time = start + 999
        result.append(bisect_right(starts, end_time) - bisect_left(ends, start_time))
        
        start_time = start - 999
        end_time = start
        result.append(bisect_right(starts, end_time) - bisect_left(ends, start_time))
        
        start_time = end
        end_time = end + 999
        result.append(bisect_right(starts, end_time) - bisect_left(ends, start_time))
        
        start_time = end - 999
        end_time = end
        result.append(bisect_right(starts, end_time) - bisect_left(ends, start_time))
        
    return max(result)
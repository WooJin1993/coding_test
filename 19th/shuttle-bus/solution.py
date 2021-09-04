# 문제: https://programmers.co.kr/learn/courses/30/lessons/17678

# --- 첫 풀이 ---
# 테스트케이스 24개 중 4개 실패

from copy import deepcopy
from heapq import heapify, heappop, heappush

def solution(n, t, m, timetable):
    timetable = [60*int(time[:2]) + int(time[3:]) for time in timetable]
    last_bus = 540 + t*(n-1)
    timetable = [(time, 0) for time in timetable if time <= last_bus]
    
    if not timetable:
        q, r = divmod(last_bus, 60)
        
        return f"{str(q).zfill(2)}:{str(r).zfill(2)}"
    
    heapify(timetable)
    result = []
    
    for arrival in range(timetable[0][0] - 1, last_bus + 1):
        table_copy = deepcopy(timetable)
        heappush(table_copy, (arrival, 1))
        shuttle = 540
        
        for _ in range(n):
            limit = m
            
            while limit:
                if table_copy[0][0] > shuttle:
                    shuttle += t
                    break
                
                _, con = heappop(table_copy)
                limit -= 1
                
                if con:
                    result.append(arrival)
                    break
            
            shuttle += t
    
    q, r = divmod(max(result), 60)
    
    return f"{str(q).zfill(2)}:{str(r).zfill(2)}"
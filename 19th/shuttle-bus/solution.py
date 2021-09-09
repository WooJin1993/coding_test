# 문제: https://programmers.co.kr/learn/courses/30/lessons/17678

# --- 첫 풀이 ---
# 테스트케이스 24개 중 4개 실패

from copy import deepcopy
from heapq import heapify, heappop, heappush

def time2num(time):
    
    return 60*int(time[:2]) + int(time[3:])

def num2time(num):
    q, r = map(str, divmod(num, 60))
    
    return f"{q.zfill(2)}:{r.zfill(2)}"
    
def solution(n, t, m, timetable):
    timetable = [time2num(time) for time in timetable]
    last_bus = 540
    
    for _ in range(n - 1):
        if last_bus + t <= 60*23 + 58:
            last_bus += t
            
    timetable = [(time, 0) for time in timetable if time <= last_bus]
    heapify(timetable)
    result = []
    
    if not timetable:
        
        return num2time(last_bus)
    
    for arrival in range(timetable[0][0] - 1, last_bus + 1):
        table_copy = deepcopy(timetable)
        heappush(table_copy, (arrival, 1))
        shuttle = 540
        
        for _ in range(n):
            limit = m
            flag = False
            
            while limit:
                if table_copy[0][0] > shuttle:
                    shuttle += t
                    break
                
                _, con = heappop(table_copy)
                limit -= 1
                
                if con:
                    result.append(arrival)
                    flag = True
                    break
            
            if flag:
                break
            
            shuttle += t
    
    return num2time(max(result))

# --- 수정된 풀이 ---

from heapq import heapify, heappop

def time2num(time):
    
    return 60*int(time[:2]) + int(time[3:])

def num2time(num):
    q, r = map(str, divmod(num, 60))
    
    return f"{q.zfill(2)}:{r.zfill(2)}"
    
def solution(n, t, m, timetable):
    timetable = [time2num(time) for time in timetable]
    last_arrival = 540 + (n-1)*t
    bus_arrival = 540
    timetable = [time for time in timetable if time <= last_arrival]
    heapify(timetable)
    
    if not timetable:
        
        return num2time(last_arrival)
    
    while bus_arrival <= last_arrival:
        limit = m
    
        while limit:
            limit -= 1
            
            if timetable[0] > bus_arrival:
                break
            
            crew_arrival = heappop(timetable)
            
            if not timetable and bus_arrival < last_arrival:
                return num2time(last_arrival)
            
            if bus_arrival == last_arrival:
                if not timetable and limit >= 1:
                    return num2time(last_arrival)
                
                if limit == 0:
                    return num2time(crew_arrival - 1)
                        
        bus_arrival += t
# 문제: https://programmers.co.kr/learn/courses/30/lessons/72414

# --- 첫 풀이 ---
# 31개 테스트 케이스 중 시간초과 18개

from bisect import bisect_left, bisect_right

def solution(play_time, adv_time, logs):
    adv_time = 3600*int(adv_time[:2]) + 60*int(adv_time[3:5]) + int(adv_time[6:])
    starts, ends = [], []
    
    for log in logs:
        start, end = log.split("-")
        start = 3600*int(start[:2]) + 60*int(start[3:5]) + int(start[6:])
        end = 3600*int(end[:2]) + 60*int(end[3:5]) + int(end[6:])
        
        starts.append(start)
        ends.append(end)
    
    starts.sort()
    ends.sort()
    result = []
    
    for start, end in zip(starts, ends):
        play_time = 0
        start_time = start
        end_time = start + adv_time
        idx1 = bisect_left(ends, start_time)
        idx2 = bisect_right(starts, end_time)
        
        for s, e in zip(starts[idx1:idx2], ends[idx1:idx2]):
            play_time += min(end_time, e) - max(start_time, s)
        
        result.append((start_time, play_time))
        
        play_time = 0
        start_time = start - adv_time
        end_time = start
        idx1 = bisect_left(ends, start_time)
        idx2 = bisect_right(starts, end_time)
        
        for s, e in zip(starts[idx1:idx2], ends[idx1:idx2]):
            play_time += min(end_time, e) - max(start_time, s)
        
        result.append((start_time, play_time))
        
        play_time = 0
        start_time = end
        end_time = end + adv_time
        idx1 = bisect_left(ends, start_time)
        idx2 = bisect_right(starts, end_time)
        
        for s, e in zip(starts[idx1:idx2], ends[idx1:idx2]):
            play_time += min(end_time, e) - max(start_time, s)
        
        result.append((start_time, play_time))
        
        play_time = 0
        start_time = end - adv_time
        end_time = end
        idx1 = bisect_left(ends, start_time)
        idx2 = bisect_right(starts, end_time)
        
        for s, e in zip(starts[idx1:idx2], ends[idx1:idx2]):
            play_time += min(end_time, e) - max(start_time, s)
        
        result.append((start_time, play_time))
        
    answer = max(result, key=lambda x: (x[1], -x[0]))[0]
    
    if answer <= 0:
        return "00:00:00"
    else:
        q1, r1 = divmod(answer, 3600)
        q2, r2 = divmod(r1, 60)
        
        return f"{str(q1).zfill(2)}:{str(q2).zfill(2)}:{str(r2).zfill(2)}"
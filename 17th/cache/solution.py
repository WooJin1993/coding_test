# 문제: https://programmers.co.kr/learn/courses/30/lessons/17680

# --- 풀이 ---

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = deque()
    total_time = 0
    
    for city in cities:
        city = city.lower()
        # Miss!
        if city not in cache:
            total_time += 5
            
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
        # Hit!
        else:
            total_time += 1
            cache.remove(city)
            cache.append(city)
    
    return total_time

# --- 다른 풀이 ---

from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    total_time = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            total_time += 1
        else:
            cache.append(city)
            total_time += 5
            
    return total_time

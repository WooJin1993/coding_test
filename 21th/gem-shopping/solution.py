# 문제: https://programmers.co.kr/learn/courses/30/lessons/67258

# --- 첫 풀이 ---

def solution(gems):
    unique_gems = set(gems)
    left = 0
    right = len(gems)
    result1 = [left + 1, right]
    
    while left < right:
        right -= 1
        
        if set(gems[left:right]) == unique_gems:
            result1[1] -= 1
        else:
            right += 1
            break
    
    while left < right:
        left += 1
        
        if set(gems[left:right]) == unique_gems:
            result1[0] += 1
        else:
            left -= 1
            break
    
    left = 0
    right = len(gems)
    result2 = [left + 1, right]
        
    while left < right:
        left += 1
        
        if set(gems[left:right]) == unique_gems:
            result2[0] += 1
        else:
            left -= 1
            break
    
    while left < right:
        right -= 1
        
        if set(gems[left:right]) == unique_gems:
            result2[1] -= 1
        else:
            right += 1
            break
    
    if len(result1) > len(result2):
        return result1
    elif len(result1) < len(result2):
        return result2
    else:
        if result1[0] <= result2[0]:
            return result1
        else:
            return result2
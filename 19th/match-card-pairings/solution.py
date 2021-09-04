# 문제: https://programmers.co.kr/learn/courses/30/lessons/72415

# --- 풀이 1 ---

from collections import deque

def solution(dartResult):
    dartResult = deque(dartResult)
    integers = list(map(str, range(10)))
    bonus = {"S": 1, "D": 2, "T": 3}
    total_score = []
    score = ""
    
    while dartResult:
        char = dartResult.popleft()
        
        if char in integers:
            score += char
        
        if char in bonus.keys():
            score = int(score)
            score **= bonus[char]
            total_score.append(score)
            score = ""
        
        if char == "*":
            total_score[-1] *= 2
            
            try:
                total_score[-2] *= 2
            except IndexError:
                pass
        
        if char == "#":
            total_score[-1] *= -1
    
    return sum(total_score)

# --- 풀이 2 ---
# 정규 표현식 이용

import re

def solution(dartResult):
    bonus_dict = {'S': 1, "D": 2, "T": 3}
    option_dict = {"": 1, "*": 2, "#": -1}
    exp = re.compile("(\d+)([SDT])([*#]?)")
    dart = exp.findall(dartResult)
    
    for i in range(len(dart)):
        score, bonus, option = dart[i]
        
        if option == "*" and i > 0:
            dart[i - 1] *= 2
            
        dart[i] = option_dict[option] * (int(score)**bonus_dict[bonus])

    return sum(dart)
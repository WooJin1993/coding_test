# 문제: https://programmers.co.kr/learn/courses/30/lessons/17687

# --- 풀이 1 ---

def convert_base(num, base):
    if num == 0:
        return "0"
    
    answer = ""
    num_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    
    while num:
        q, r = divmod(num, base)
        num = q
        
        if r >= 10:
            r = num_dict[r]
        
        if r:
            answer += str(r)
        else:
            answer += "0"
    
    return answer[::-1]

def solution(n, t, m, p):
    total = ""
    answer = ""
    num = 0
    idx = p - 1
    
    while len(total) < t * m:
        total += convert_base(num, base=n)
        num += 1
    
    while len(answer) < t:
        answer += total[idx]
        idx += m
    
    return answer

# --- 풀이 2 ---
# conver_base를 재귀적으로 만듦

def convert_base(num, base):
    digits = "0123456789ABCDEF"
    q, r = divmod(num, base)
    
    if q == 0:
        return digits[r]
    else:
        return convert_base(q, base) + digits[r]
    
def solution(n, t, m, p):
    total = ""
    answer = ""
    num = 0
    idx = p - 1
    
    while len(total) < t * m:
        total += convert_base(num, base=n)
        num += 1
    
    while len(answer) < t:
        answer += total[idx]
        idx += m
    
    return answer
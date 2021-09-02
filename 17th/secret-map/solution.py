# 문제: https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    result = []
    
    for x, y in zip(arr1, arr2):
        bin_num = bin(x | y)[2:].zfill(n)
        result.append(bin_num.replace("1", "#").replace("0", " "))
    
    return result

# --- 다른 풀이 ---

def solution(n, arr1, arr2):
    result = []
    
    for x, y in zip(arr1, arr2):
        bin_num = bin(x | y)[2:].zfill(n)
        result.append(bin_num.translate({ord("1"): ord("#"), ord("0"): ord(" ")}))
    
    return result
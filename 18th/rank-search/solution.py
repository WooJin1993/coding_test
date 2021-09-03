# 문제: https://programmers.co.kr/learn/courses/30/lessons/72412

# --- 첫 풀이 ---
# 효율성 전부 실패

from operator import itemgetter

def count_filtered_row(info, q):
    condition = q[:-1]
    score = int(q[-1])
    
    # 조건이 있는 column index
    condition_idx = [i for i, x in enumerate(condition) if x != "-"]
    condition = [x for x in condition if x != "-"]
    
    # 조건에 해당하는 데이터 개수 세기
    score_info = [x[-1] for x in info]
    score_idx = []
    
    for i, x in enumerate(score_info):
        if int(x) >= score:
            score_idx.append(i)
    
    if not score_idx:
        return 0
    
    filtered_info = list(itemgetter(*score_idx)(info))
    
    if len(condition_idx) == 0:
        return len(filtered_info)
    elif len(condition_idx) == 1:
        if type(filtered_info[0]) != list:
            filtered_info = filtered_info[condition_idx[0]]
            
            if filtered_info == condition[0]:
                return 1
            else:
                return 0
        else:
            filtered_info = [list(col) for col in zip(*filtered_info)]
            filtered_info = filtered_info[condition_idx[0]]
            filtered_info = [x for x in filtered_info if x == condition[0]]
            
            return len(filtered_info)
    else:
        if type(filtered_info[0]) != list:
            filtered_info = list(itemgetter(*condition_idx)(filtered_info))
            
            if filtered_info == condition:
                return 1
            else:
                return 0
        else:
            filtered_info = [list(col) for col in zip(*filtered_info)]
            filtered_info = list(itemgetter(*condition_idx)(filtered_info))
            filtered_info = [list(col) for col in zip(*filtered_info)]
            filtered_info = [x for x in filtered_info if x == condition]
            
            return len(filtered_info)

def solution(info, query):
    result = []
    
    for i, x in enumerate(info):
        info[i] = x.split(" ")
    
    for i, q in enumerate(query):
        query[i] = [x for x in q.split(" ") if x != "and"]

    for q in query:
        result.append(count_filtered_row(info, q))
            
    return result

# --- 두 번째 풀이 ----

from bisect import bisect_left
from collections import defaultdict
from itertools import product

def solution(info, query):
    info_dict = defaultdict(list)
    result = []
    
    for x in info:
        lang, pos, career, food, score = x.split()
        
        for key in product((lang, "-"), (pos, "-"), (career, "-"), (food, "-")):
            key = " and ".join(key)
            info_dict[key].append(int(score))
            
    for q in query:
        q = q.split()
        key = " ".join(q[:-1])
        score = int(q[-1])
        
        value = info_dict[key]
        result.append(len(value) - bisect_left(sorted(value), score))
    
    return result
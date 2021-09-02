# 문제: https://programmers.co.kr/learn/courses/30/lessons/42888

# --- 처음 풀이 ---
# 1개 시간초과

def separate_change(record):
    change_dict = dict()
    
    for r in record.copy():
        r_splited = r.split()
        
        if r_splited[0] == "Enter":
            change_dict[r_splited[1]] = r_splited[2]
        elif r_splited[0] == "Change":
            change_dict[r_splited[1]] = r_splited[2]
            record.remove(r)
        
    return record, change_dict

def solution(record):
    record, change_dict = separate_change(record)
    
    for i, r in enumerate(record):
        action, uid = r.split()[:2]
        nickname = change_dict[uid]
        
        if action == "Enter":
            record[i] = f"{nickname}님이 들어왔습니다."
        else:
            record[i] = f"{nickname}님이 나갔습니다."
        
    return record

# --- 수정된 풀이 ---

def separate_change(record):
    nickname_dict = dict()
    new_record = []
    
    for r in record:
        r_splited = r.split()
        
        if r_splited[0] == "Enter":
            nickname_dict[r_splited[1]] = r_splited[2]
            new_record.append(("E", r_splited[1]))
        elif r_splited[0] == "Leave":
            new_record.append(("L", r_splited[1]))
        else:
            nickname_dict[r_splited[1]] = r_splited[2]
        
    return new_record, nickname_dict

def solution(record):
    record, nickname_dict = separate_change(record)
    
    for i, r in enumerate(record):
        action, uid = r
        nickname = nickname_dict[uid]
        
        if action == "E":
            record[i] = f"{nickname}님이 들어왔습니다."
        else:
            record[i] = f"{nickname}님이 나갔습니다."
        
    return record
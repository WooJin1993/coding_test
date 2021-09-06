from collections import Counter

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=50:
        return "D"
    else:
        return "F"

def get_mean_score(column, i):
    score_counter = Counter(column)
    
    if column[i] == max(column) or column[i] == min(column):
        if score_counter[column[i]] == 1:
            column.pop(i)
            
    return sum(column) / len(column)

def solution(scores):
    answer = ""
    
    for i, column in enumerate(zip(*scores)):
        mean_score = get_mean_score(list(column), i)
        answer += assign_grade(mean_score)
    
    return answer
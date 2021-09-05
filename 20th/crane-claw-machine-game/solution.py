# 문제: https://programmers.co.kr/learn/courses/30/lessons/64061

# --- 풀이 1 ---

def solution(board, moves):
    board = list(map(list, zip(*board)))
    basket = []
    answer = 0
    
    for move in moves:
        column = board[move - 1]
        
        for i in range(len(board)):
            if column[i] != 0:
                if basket and basket[-1] == column[i]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(column[i])
                    
                column[i] = 0
                break    

    return answer

# --- 풀이 2 ---

from collections import deque

def solution(board, moves):
    board = [deque(filter(lambda x: x > 0, col)) for col in zip(*board)]
    basket = []
    answer = 0
    
    for move in moves:
        column = board[move - 1]
        
        if not column:
            continue
        
        doll = column.popleft()
        
        if basket and basket[-1] == doll:
            basket.pop()
            answer += 2
        else:
            basket.append(doll)
        
    return answer

# --- 풀이 3 ---
# 바다코끼리 연산자(:=) 사용

from collections import deque

def solution(board, moves):
    board = [deque(filter(lambda x: x > 0, col)) for col in zip(*board)]
    basket = []
    answer = 0
    
    for move in moves:
        if not (column := board[move - 1]):
            continue
        
        doll = column.popleft()
        
        if basket and basket[-1] == doll:
            basket.pop()
            answer += 2
        else:
            basket.append(doll)
        
    return answer

# --- 풀이 4 ---
# 윤응구 풀이

def solution(board, moves):
    cols = [list(filter(lambda x: x > 0, col)) for col in zip(*board)]
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a
def check(place, x, y):
    # step 0 (manhattan = 1)
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dirs2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for dx, dy in dirs:
        P_x, P_y = x + dx, y + dy
        if 0 <= P_x <= 4 and 0 <= P_y <= 4:
            if place[P_x][P_y] == "P":
                return False
            
    # step 1 ~ 4 (left, right, up, down)
    for dx, dy in dirs:
        P_x, P_y = x + 2*dx, y + 2*dy
        X_x, X_y = x + dx, y + dy
        
        if not (0 <= P_x <= 4 and 0 <= P_y <= 4):
            continue
        if place[P_x][P_y] == "P" and place[X_x][X_y] != "X":
            return False
    
    # step 5 ~ 8 (down-right, down-left, up-right, up-left)
    for dx, dy in dirs2:
        P_x, P_y = x + dx, y + dy
        X1_x, X1_y = x + dx, y
        X2_x, X2_y = x, y + dy
        
        if not (0 <= P_x <= 4 and 0 <= P_y <= 4):
            continue
        if place[P_x][P_y] == "P" and (place[X1_x][X1_y] != "X" or place[X2_x][X2_y] != "X"):
            return False
    
    return True
            
def is_correct(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if not check(place, i, j):
                    return 0
    
    return 1

def solution(places):
    for place in places:
        for i, p in enumerate(place):
            place[i] = list(p)
    
    result = []
    
    for place in places:
        result.append(is_correct(place))
    
    return result

# --- 첫 풀이 ---

def check(place, x, y):
    # step 0 (manhattan = 1)
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            if place[nx][ny] == "P":
                return False
        
    # step 1 (left)
    nx, ny = x, y - 2
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx][ny + 1] != "X":
                return False
    # step 2 (right)
    nx, ny = x, y + 2
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx][ny - 1] != "X":
                return False
    # step 3 (up)
    nx, ny = x - 2, y
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx + 1][ny] != "X":
                return False
    # step 4 (down)
    nx, ny = x + 2, y
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx - 1][ny] != "X":
                return False
    # step 5 (up-left)
    nx, ny = x - 1 , y - 1
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx][ny + 1] != "X" or place[nx + 1][ny] != "X":
                return False
    # step 6 (up-right)
    nx, ny = x - 1 , y + 1
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx][ny - 1] != "X" or place[nx + 1][ny] != "X":
                return False
    # step 7 (down-left)
    nx, ny = x + 1 , y - 1
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx][ny + 1] != "X" or place[nx - 1][ny] != "X":
                return False
    # step 8 (down-right)
    nx, ny = x + 1 , y + 1
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        if place[nx][ny] == "P":
            if place[nx][ny - 1] != "X" or place[nx - 1][ny] != "X":
                return False
    
    return True
            
def is_correct(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if not check(place, i, j):
                    return 0
    
    return 1

def solution(places):
    for place in places:
        for i, p in enumerate(place):
            place[i] = list(p)
    
    result = []
    
    for place in places:
        result.append(is_correct(place))
    
    return result
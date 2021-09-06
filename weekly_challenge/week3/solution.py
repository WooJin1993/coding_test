def get_rotated(matrix):

    return [list(reversed(m)) for m in zip(*matrix)]

def get_expanded(game_board):
    N = len(game_board)
    expanded = [[1] * (N+2) for _ in range(N + 2)]
    
    for x in range(N):
        for y in range(N):
            expanded[1 + x][1 + y] = game_board[x][y]
    
    return expanded

def can_fill(puzzle, expanded):
    M, N = len(puzzle), len(expanded)
    N -= 2
    
    def check(x, y):
        for i in range(M):
            for j in range(M):
                if puzzle[i][j] == 1:
                    if expanded[x + i][y + j] == 0 and expanded[x + i][y + j] == 0
                
                
                
        return 
    
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            
    
            
    

def extract_puzzle(table):
    

def solution(game_board, table):
    answer = -1
    return answer


# --- 모범 답안 ---

from collections import Counter
from dataclasses import dataclass
from itertools import product

@dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def neighbors(self):
        
        return [
            Pos(self.x, self.y - 1),
            Pos(self.x + 1, self.y),
            Pos(self.x, self.y + 1),
            Pos(self.x - 1, self.y),
        ]

def get_rotated(matrix):

    return tuple(tuple(reversed(m)) for m in zip(*matrix))

def make_tile_from_positions(positions):
    # Smallest possible representation with rotation
    positions = set(positions)

    xs = [pos.x for pos in positions]
    min_x = min(xs)
    max_x = max(xs)

    ys = [pos.y for pos in positions]
    min_y = min(ys)
    max_y = max(ys)

    tile_representations = [
        tuple(
            tuple(Pos(i, j) in positions for j in range(min_y, max_y + 1)) for i in range(min_x, max_x + 1)
        )
    ]

    for __ in range(3):
        tile_representations.append(get_rotated(tile_representations[-1]))

    return min(tile_representations)

def get_tile_size(tile):
    
    return sum(sum(row) for row in tile)

def parse_tiles(board, tile_value=1):
    n = len(board)

    # Add sentinel boundaries
    sentinel = 1 - tile_value

    board = [
        [sentinel] * (n + 2),
        *([sentinel] + row + [sentinel] for row in board),
        [sentinel] * (n + 2),
    ]

    # Detect tiles
    tile_positions = []
    
    for i, j in product(range(1, n + 1), range(1, n + 1)):
        if board[i][j] == tile_value:
            stack = [Pos(i, j)]
            squares = []
            
            while stack:
                curr = stack.pop()
                board[curr.x][curr.y] = sentinel
                squares.append(curr)
                
                for neighbor in curr.neighbors():
                    if board[neighbor.x][neighbor.y] == tile_value:
                        stack.append(neighbor)
                        
            tile_positions.append(squares)

    # Make tiles
    tiles = [make_tile_from_positions(p) for p in tile_positions]

    return tiles

def solution(game_board, table):
    tiles = parse_tiles(table, 1)
    empty_spaces = parse_tiles(game_board, 0)

    tile_counter = Counter(tiles)
    empty_space_counter = Counter(empty_spaces)

    used_tiles = tile_counter & empty_space_counter

    return sum(get_tile_size(tile) * occ for tile, occ in used_tiles.items())

# --- 모범 답안 2 ---

from collections import defaultdict, deque
# 아래, 오른쪽, 위, 왼쪽
x_move = [1,0,-1,0]
y_move = [0,1,0,-1]
dirs = [(0, 1), (1, 0) , (0, -1), (-1, 0)]
table_num_dict = defaultdict(list)
board_num_dict = defaultdict(list)

def bfs(table, table_num, init, x, y):
    n = len(table)
    queue = deque()
    queue.append((x, y))
    table[x][y] = table_num
    tmp_path = [x, y]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    if init == False:
        visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            
            if init == True and table[nx][ny] == 1:
                queue.append((nx, ny))
                table[nx][ny] = table_num
                tmp_path.extend((nx, ny))
                
            if init == False and visited[nx][ny] != 1 and table[nx][ny] == table_num:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                tmp_path.extend((nx, ny))
                    
    table_num_dict[table_num].append(tmp_path)

    
def board_bfs(board, board_num, x, y):
    q = deque()
    q.append([x,y])
    board[x][y] = board_num
    tmp_path = [x,y]
    
    while q:
        now_x, now_y = q.popleft()
        
        for i in range(len(x_move)):
            next_x, next_y = now_x+x_move[i], now_y+y_move[i]
            if 0 <= next_x < len(board) and 0 <= next_y < len(board):
                if board[next_x][next_y] == 0:
                    q.append([next_x, next_y])
                    board[next_x][next_y] = board_num
                    tmp_path.extend([next_x, next_y])
                    
    board_num_dict[board_num].append(tmp_path)


def table_rotate(table):
    tmp_table = [[0 for y in range(len(table))] for x in range(len(table))]
    for x in range(len(tmp_table)):
            for y in range(len(tmp_table)):
                tmp_table[y][len(table)-1-x] = table[x][y]
    return tmp_table


def solution(game_board, table):
    answer = 0
    
    #table num 2부터
    table_num = 2
    for x in range(len(table)):
        for y in range(len(table)):
            if table[x][y] == 1:
                bfs(table, table_num, True, x, y)
                table_num += 1
    
    # 3번 돌림
    for i in range(3): 
        table = table_rotate(table)
        table_num_visited = []
        for x in range(len(table)):
            for y in range(len(table)):
                if table[x][y] >= 2 and table[x][y] not in table_num_visited:
                    table_num = table[x][y]
                    table_num_visited.append(table_num)
                    bfs(table, table_num, False, x, y)
                    
    #board
    board_num = 2
    for x in range(len(game_board)):
        for y in range(len(game_board)):
            if game_board[x][y] == 0:
                board_bfs(game_board, board_num, x, y)
                board_num += 1 
    
    table_num_visited = []
    for i in range(len(board_num_dict)):
        board_cmp = board_num_dict[i+2][0]
        find_answer = False
        for j in range(len(table_num_dict)):
            if (j+2) in table_num_visited:
                continue
            if find_answer == True:
                break
            for k in range(4):
                table_cmp = table_num_dict[j+2][k]    
                if len(board_cmp) != len(table_cmp):
                    break
                if len(board_cmp) == 1 and len(table_cmp) == 1:
                    answer += 1
                    find_answer = True
                    table_num_visited.append(j+2)
                    break
                
                cmp_right = True
                cmp_first, cmp_second = board_cmp[0]-table_cmp[0], board_cmp[1]-table_cmp[1]
                for l in range(2, len(board_cmp)):
                    if l%2 == 0 and board_cmp[l]-table_cmp[l] != cmp_first:
                        cmp_right = False
                        break
                    if l%2 == 1 and board_cmp[l]-table_cmp[l] != cmp_second:
                        cmp_right = False
                        break
                
                if cmp_right == True:
                    answer += len(table_cmp)//2
                    find_answer = True
                    table_num_visited.append(j+2)
                    break
            
    return answer
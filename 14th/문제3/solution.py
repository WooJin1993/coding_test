# --- 첫 풀이 ---
# 정확성만 성공
# 효율성 전부 실패

def solution(n, k, cmd):
    delete = []
    
    for s in cmd:             
        if s[0] == "D":
            for _ in range(int(s[2:])):
                k += 1
                while k in delete:
                    k += 1
        elif s[0] == "U":
            for _ in range(int(s[2:])):
                k -= 1
                while k in delete:
                    k -= 1
        elif s == "C":
            delete.append(k)
            
            if k == n - 1:
                k -= 1
                while k in delete:
                    k -= 1
            elif set(range(k + 1, n)) <= set(delete):
                k -= 1
                while k in delete:
                    k -= 1
            else:
                k += 1
                while k in delete:
                    k += 1
        else:
            delete.pop()
            
    result = n * ["O"]
    
    for i in delete:
        result[i] = "X"
    
    return "".join(result)

# --- heap을 이용한 풀이 1 ---

from heapq import heappop, heappush

def solution(n, k, cmd):
    # 현재 위치: right heap의 첫 번째 원소
    left, right, delete = [], [], []
    
    # 왼쪽은 최댓값이 맨 앞에 위치하도록, 오른쪽은 최솟값이 맨 앞에 위치하도록 heap을 구성한다.
    for i in range(n):
        heappush(right, i)
    
    for _ in range(k):
        heappush(left, -heappop(right))
        
    for c in cmd:
        # 현재 선택된 행에서 move칸만큼 아래로 내려가는 경우
        if c[0] == "D":
            move = int(c.split()[-1])
            
            for _ in range(move):
                # 오른쪽 heap에서 왼쪽 heap으로 값을 이동시킨다.
                heappush(left, -heappop(right))
        # 현재 선택된 행에서 move칸만큼 위로 내려가는 경우
        elif c[0] == "U":
            move = int(c.split()[-1])
            
            for _ in range(move):
                # 왼쪽 heap에서 오른쪽 heap으로 값을 이동시킨다.
                heappush(right, -heappop(left))
        # 현재 선택된 행을 삭제하는 경우
        elif c == "C":
            # 값을 삭제하되 가장 최근에 삭제된 값을 복구하기 쉽도록 stack을 사용한다.
            delete.append(heappop(right))
            
            if not right:
                # 삭제된 행이 가장 마지막행인 경우 바로 윗 행을 선택하도록 한다.
                heappush(right, -heappop(left))
        # 가장 최근에 삭제된 행을 원래대로 복구하는 경우
        else:
            # 삭제된 값 복구하기
            repair = delete.pop()
            
            # 현재 위치보다 값이 작을 경우 left에 넣는다.
            if repair < right[0]:
                heappush(left, -repair)
            else:
                heappush(right, repair)
        
    result = ["O"] * n
    
    for i in delete:
        result[i] = "X"
    
    return "".join(result)

# --- heap을 이용한 풀이 2 ---

from heapq import heappop, heappush

def get_refined_cmd(cmd):
    refined_cmd = []
    result = 0
    
    for c in cmd:
        if c[0] == "D":
            result += int(c[2:])
        elif c[0] == "U":
            result -= int(c[2:])
        else:
            if result:
                refined_cmd.append(result)
                
            result = 0
            refined_cmd.append(c)
    
    return refined_cmd

def solution(n, k, cmd):
    # 현재 위치: right heap의 첫 번째 원소
    left, right, delete = [], [], []
    
    # 왼쪽은 최댓값이 맨 앞에 위치하도록, 오른쪽은 최솟값이 맨 앞에 위치하도록 heap을 구성한다.
    for i in range(n):
        heappush(right, i)
    
    for _ in range(k):
        heappush(left, -heappop(right))
    
    cmd = get_refined_cmd(cmd)
    
    for c in cmd:
        if isinstance(c, int):
            # 현재 선택된 행에서 move칸만큼 아래로 내려가는 경우
            if c > 0:
                for _ in range(c):
                    # 오른쪽 heap에서 왼쪽 heap으로 값을 이동시킨다.
                    heappush(left, -heappop(right))
            # 현재 선택된 행에서 move칸만큼 위로 내려가는 경우
            elif c < 0:
                for _ in range(-c):
                    # 왼쪽 heap에서 오른쪽 heap으로 값을 이동시킨다.
                    heappush(right, -heappop(left))
        # 현재 선택된 행을 삭제하는 경우
        elif c == "C":
            # 값을 삭제하되 가장 최근에 삭제된 값을 복구하기 쉽도록 stack을 사용한다.
            delete.append(heappop(right))
            
            if not right:
                # 삭제된 행이 가장 마지막행인 경우 바로 윗 행을 선택하도록 한다.
                heappush(right, -heappop(left))
        # 가장 최근에 삭제된 행을 원래대로 복구하는 경우
        else:
            # 삭제된 값 복구하기
            repair = delete.pop()
            
            # 현재 위치보다 값이 작을 경우 left에 넣는다.
            if repair < right[0]:
                heappush(left, -repair)
            else:
                heappush(right, repair)
        
    result = ["O"] * n

    for i in delete:
        result[i] = "X"

    return "".join(result)

# --- LinkedList를 이용한 풀이 1 ---
# Node 클래스 구현

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def solution(n, k, cmd):
    delete = []
    nodes = [Node(i) for i in range(n)]

    for i in range(1, n - 1):
        nodes[i].left = nodes[i - 1]
        nodes[i - 1].right = nodes[i]
        
        nodes[i].right = nodes[i + 1]
        nodes[i + 1].left = nodes[i]

    cur_node = nodes[k]
    
    for c in cmd:
        if c[0] == "D":
            move = int(c.split()[-1])
            
            for _ in range(move):
                cur_node = cur_node.right
        elif c[0] == "U":
            move = int(c.split()[-1])
            
            for _ in range(move):
                cur_node = cur_node.left
        elif c == "C":
            delete.append(cur_node)
            left_node, right_node = cur_node.left, cur_node.right

            if left_node:
                left_node.right = right_node
            
            if right_node:
                cur_node = right_node
                right_node.left = left_node
            else:
                cur_node = left_node
        else:
            repair = delete.pop()
            left_node, right_node = repair.left, repair.right

            if left_node:
                left_node.right = repair

            if right_node:
                right_node.left = repair

    result = ["O"] * n

    for node in delete:
        result[node.value] = "X"

    return "".join(result)

# --- LinkedList를 이용한 풀이 2 ---
# list로 LinkedList 구현
# 런타임 에러 3개

def solution(n, k, cmd):
    current = k
    Llist = [[i - 1, i + 1] for i in range(n)] # current 위치에 [prev, next]를 저장 (LinkedList 구현 목적)
    delete = []
    
    for c in cmd:
        if c[0] == "D":
            move = int(c.split()[-1])
            
            for _ in range(move):
                current = Llist[current][1]
        elif c[0] == "U":
            move = int(c.split()[-1])
            
            for _ in range(move):
                current = Llist[current][0]
        elif c == "C":
            delete.append(current)
            left, right = Llist[current]
            
            if right == n: # 삭제된 행이 가장 마지막 행인 경우
                current = left
                Llist[left][1] = right
            else:
                current = right
                Llist[right][0] = left
                
                if left >= 0:
                    Llist[left][1] = right
        else:
            repair = delete.pop()
            left, right = Llist[repair]
            
            if left >= 0:
                Llist[left][1] = repair
                
            if right <= n - 1:
                Llist[right][0] = repair

    result = ["O"] * n
    
    for i in delete:
        result[i] = "X"
        
    return "".join(result)

# --- LinkedList를 이용한 풀이 3 ---
# dict로 LinkedList 구현

def solution(n, k, cmd):
    current = k
    Llist = dict()
    
    for i in range(n):
        Llist[i] = [i - 1, i + 1]
    
    Llist[0][0] = Llist[n - 1][1] = None
    delete = []

    for c in cmd:
        if c == "C":
            left, right = Llist[current]
            delete.append(current)
            
            if right is None: # 삭제된 행이 가장 마지막 행인 경우
                current = left
                Llist[left][1] = None
            else:
                current = right
                Llist[right][0] = left
                
                if left is not None:
                    Llist[left][1] = right    
        elif c == "Z":
            repair = delete.pop()
            left, right = Llist[repair]
            
            if left is not None:
                Llist[left][1] = repair
                
            if right is not None:
                Llist[right][0] = repair
        else:
            move = int(c.split()[-1])
            
            for _ in range(move):
                current = Llist[current][int(c[0] == "D")]

    result = ["O"] * n
    
    for i in delete:
        result[i] = "X"
        
    return "".join(result)
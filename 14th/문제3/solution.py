# def get_refined_cmd(cmd):
#     refined_cmd = []
#     result = 0
    
#     for c in cmd:
#         if c[0] == "D":
#             result += int(c[2:])
#         elif c[0] == "U":
#             result -= int(c[2:])
#         else:
#             if result:
#                 refined_cmd.append(result)
                
#             result = 0
#             refined_cmd.append(c)
    
#     return refined_cmd

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList: 
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
    
#     def add(self, data):
#         new_node = Node(data)
        
#         if not self.head:
#             self.head = new_node
#             self.tail = self.head
#         else:
#             node = self.head
            
#             while node.next:
#                 node = node.next
            
#             new_node.prev = node
#             node.next = new_node
#             self.tail = new_node
    
#     def delete(self, data):
#         node = self.head
    
#         if node.data == data:
#             self.head = node.next
#             del node
#         else:
#             while node.next:
#                 next_node = node.next
                
#                 if next_node.data == data:
#                     node.next = next_node.next
#                     del next_node
#                 else:
#                     node = node.next
    
#     def find(self, data):
#         node = self.head
        
#         while node:
#             if node.data == data:
#                 return node
#             else:
#                 node = node.next
    
#     def print(self):
#         node = self.head
        
#         while node:
#             print(node.data)
#             node = node.next

class Node(object):
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
    
    def listSize(self):
        return self.size
    
    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
    
    def selectNode(self, idx):
        if idx > self.size:
            print("Overflow: Index Error")
            return None
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        if idx <= self.size//2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail
            for _ in range(self.size - idx):
                target = target.prev
            return target
    
    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(value, None, self.head)
            tmp.prev = self.head
        self.size += 1
            
    
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(value, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1
    
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(value)
            elif tmp == self.tail:
                self.append(value)
            else:
                tmp_prev = tmp.prev
                newNode = Node(value, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
        self.size += 1
        
    def delete(self, idx):
        if self.is_empty():
            print("Underflow Error")
            return
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
            else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del(tmp)
            self.size -= 1
    
    def printlist(self):
        target = self.head
        while target != self.tail:
            if target.next != self.tail:
                print(target.data, '<=> ', end='')
            else:
                print(target.data)
            target = target.next

def solution(n, k, cmd):
    llist = DList()
    removed = []
    
    for i in range(n):
        llist.add(i)
    
    node = llist.find(k)
    
    for c in cmd:
        if c[0] == "D":
            for _ in range(int(c[2:])):
                node = node.next
        elif c[0] == "U":
            for _ in range(int(c[2:])):
                node = node.prev
        elif c == "C":
            idx = node.data
            llist.delete(idx)
            node = node.next
            
            if node is None:
                node = llist.find(idx - 1)
            
            removed.append(idx)
        else:
            new_idx = removed.pop()
            

# --- 첫 풀이 ---
# 효율성 전부 실패

def solution(n, k, cmd):
    del_idx = []
    
    for s in cmd:             
        if s[0] == "D":
            for _ in range(int(s[2:])):
                k += 1
                while k in del_idx:
                    k += 1
        elif s[0] == "U":
            for _ in range(int(s[2:])):
                k -= 1
                while k in del_idx:
                    k -= 1
        elif s == "C":
            del_idx.append(k)
            
            if k == n - 1:
                k -= 1
                while k in del_idx:
                    k -= 1
            elif set(range(k + 1, n)) <= set(del_idx):
                k -= 1
                while k in del_idx:
                    k -= 1
            else:
                k += 1
                while k in del_idx:
                    k += 1
        else:
            del_idx.pop()
            
    result = n * ["O"]
    
    for idx in del_idx:
        result[idx] = "X"
    
    return "".join(result)

# --- heap을 이용한 풀이1 ---

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

# --- heap을 이용한 풀이2 ---

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
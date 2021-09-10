# 문제: https://programmers.co.kr/learn/courses/30/lessons/42892

import sys

sys.setrecursionlimit(1500)

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def add_node(parent, child):
    if parent.x > child.x:
        if parent.left is None:
            parent.left = child
        else:
            add_node(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            add_node(parent.right, child)

def preorder(answer, root):
    if root is None:
        return
    
    answer.append(root.id)
    preorder(answer, root.left)
    preorder(answer, root.right)

def postorder(answer, root):
    if root is None:
        return
    
    postorder(answer, root.left)
    postorder(answer, root.right)
    answer.append(root.id)

def solution(nodeinfo):
    node_list = []
    
    for i, info in enumerate(nodeinfo):
        node_list.append(Node(i + 1, info[0], info[1]))
    
    node_list.sort(key=lambda node: (-node.y, node.x))
    root = node_list[0]
    
    for child in node_list[1:]:
        add_node(root, child)
    
    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)
    
    return answer
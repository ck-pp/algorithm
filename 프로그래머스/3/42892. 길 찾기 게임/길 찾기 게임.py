import sys
sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None
    
def solution(nodeinfo):
    res = [[], []]  # 전위 순회, 후위 순회 결과
    
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda xy: (-xy[1], xy[0]))  # y 내림차순, x 오름차순

    g = [Node(x, y, idx) for x, y, idx in nodes]
    
    # 트리 구성
    def tree_insert(parent, child):
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                tree_insert(parent.left, child)    
        else:
            if parent.right is None:
                parent.right = child
            else:
                tree_insert(parent.right, child)
    
    root = g[0]
    for node in g[1:]:
        tree_insert(root, node)
    
    # 전위, 후위 순회 결과 저장 함수(재귀)
    def recurOrder(node):
        if node is None:
            return
        res[0].append(node.idx)
        recurOrder(node.left)  # 왼쪽 자식 노드 탐색
        recurOrder(node.right)  # 오른쪽 자식 노드 탐색
        res[1].append(node.idx)
    
    recurOrder(root)
        
    return res
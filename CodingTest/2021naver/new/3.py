from collections import deque
class Node:
  def __init__(self, id):
    self.id = id
    self.child = []
    self.nChild = 0

def find(root, id):
  for c in root.child:
    if c.id == id:
      root.nChild += 1
      return c
  
  for c in root.child:
    f = find(c, id)    
    if type(f) == Node:
      root.nChild += 1
      return f
  
  return None

def add(root, parent, child):
  if parent == 0:
    root.child.append(Node(child))
    return
  p = find(root, parent)
  p.child.append(Node(child))

def pprint(root):
  print(root.id, root.nChild)
  for child in root.child:
    pprint(child)

def calculate_child(root):
  root.nChild += len(root.child)
  for child in root.child:
    calculate_child(child)
  

def infect(root):
  
  return 0
  
def solution(n, edges):
  root = Node(0)
  edges.sort()
  for edge in edges:
    add(root, edge[0], edge[1])
  
  calculate_child(root)
  q = deque([(root, 0)])
  cnt = 0
  while q:
    levels = []
    node, level = q.popleft()
    cnt += 1
    levels.append(node)
    while q and q[0][1] == level:
      cnt += 1
      levels.append(q.popleft()[0])
    M = 0
    M_i = 0
    children = []
    for p in levels:
      children.extend(p.child)
    
    for i in range(len(children)):
      if children[i].nChild > M and len(children[i].child) > 1:
        M_i = i
        M = children[i].nChild
    # print('부모: %d, 버리는 자식: %d'%(node.id, children[M_i].id))
    for i in range(len(children)):
      if i==M_i: continue
      q.append((children[i], level+1))
    
    # print('cnt: ',cnt)

  return cnt

print(solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
print(solution(14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]))
print(solution(10, [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]))
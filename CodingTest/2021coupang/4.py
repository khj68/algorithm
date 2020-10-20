from collections import defaultdict

def solution(depar, hub, dest, roads):
  
  to_hub = to_dest = 0
  nodes = defaultdict(list)

  for s, e in roads:
    nodes[s].append(e)
  
  def dfs(depar, dest):
    nonlocal cnt
    # print(depar, dest)
    for node in nodes[depar]:
      if node == dest:
        cnt += 1
      else :
        dfs(node, dest)

  cnt = 0
  dfs(depar, hub)
  to_hub = cnt

  cnt = 0
  dfs(hub, dest)
  to_dest = cnt
  

  return (to_hub * to_dest) % 10007




print(solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
print(solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]))
# print(solution())
def solution(blocks):
  ans = [[0]*(i+1) for i in range(len(blocks))]
  ans[0][0] = blocks[0][1]
  print(ans)
  for i in range(1, len(blocks)):
    k, num = blocks[i]
    ans[i][k] = num
    for j in range(k-1, -1, -1):
      ans[i][j] = ans[i-1][j] - ans[i][j+1]
    for j in range(k+1, len(ans[i])):
      ans[i][j] = ans[i-1][j-1] - ans[i][j-1]
  print(ans)
  answer = []
  for li in ans:
    answer += li
  return answer


print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))
# print(solution())
# print(solution())
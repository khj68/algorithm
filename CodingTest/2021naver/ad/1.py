def solution(A):
  cur = A[0]
  ans = 1
  while cur != -1:
    cur = A[cur]
    ans += 1
  return ans





print(solution([1,4,-1,3,2]))
# print(solution())
# print(solution())
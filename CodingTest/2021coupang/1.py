def solution(n):
  ans = [0, 0]
  for i in range(2, 10):
    cur = n
    tmp = 1
    while cur:
      tmp *= cur % i if cur %i != 0 else 1
      cur //= i
    
    if tmp >= ans[1]:
      ans[1] = tmp
      ans[0] = i
  

  return ans




print(solution(10))
print(solution(14))
print(solution(1000000))
# print(solution())
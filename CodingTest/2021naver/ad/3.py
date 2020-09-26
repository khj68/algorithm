def solution(T):
  left, right= 0, len(T)-1
  M, m = T[left], T[right]

  while right > 0:
    right -= 1
    if T[right] < m:
      m = T[right]
    
    if m < M:
      break
  
  
  return right+1






print(solution([5, -2, 3, 8, 6]))
# print(solution([5, -2, 3, 8, 6, 9]))
print(solution([-5, -5, -5, -42, 6, 12]))
print(solution([5,6,3,2,1,7]))
print(solution([1,2,3,4,5,6]))
print(solution([1, 100, -3, -6000, -2000, 60000]))
print(solution([-5, -5, -5, -42, 6, 12, 50]))
# print(solution())
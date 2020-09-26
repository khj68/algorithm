def solution(T):
  winterM = T[0]
  yearM = T[0]
  ans = 1

  for i, t in enumerate(T):
    if t < winterM :
      ans = i+1
      winterM = yearM
    elif t > yearM:
      yearM = t
  
  if ans == len(T):
    return ans-1
  
  return ans






print(solution([5, -2, 3, 8, 6]))
# print(solution([5, -2, 3, 8, 6, 9]))
print(solution([-5, -5, -5, -42, 6, 12]))
print(solution([5,6,3,2,1,7]))
print(solution([1,2,3,4,5,6]))
print(solution([1, 100, -3, -6000, -2000, 60000]))
print(solution([-5, -5, -5, -42, 6, 12, 50]))
# print(solution())
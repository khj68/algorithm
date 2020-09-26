def solution(nums):
  def solve(isOne):
    cnt = 0
    for num in nums:
      if isOne and num != isOne:
        cnt += 1
      
      if not isOne and num != 0:
        cnt += 1
      
      isOne = 0 if isOne else 1
    return cnt
  
  return min(solve(1), solve(0))



print(solution([1,0,1,0,1,1]))
print(solution([1,1,0,1,1]))
print(solution([0,1,0]))
print(solution([0,1,1,0]))
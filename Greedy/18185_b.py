n = int(input())

nums = list(map(int, input().split()))
ans = 0
nums.extend([0,0])
def three(i):
  global ans
  while(nums[i] and nums[i+1] and nums[i+2]):
    nums[i] -= 1
    nums[i+1] -= 1
    nums[i+2] -= 1
    ans += 7

def two(i):
  global ans
  while(nums[i] and nums[i+1]):
    nums[i] -= 1
    nums[i+1] -= 1
    ans += 5

def one(i):
  global ans
  ans += 3*nums[i]

for i in range(n):
  if nums[i+1] > nums[i+2] :
    m = min(nums[i], nums[i+1]-nums[i+2])
    nums[i] -= m
    nums[i+1] -= m
    ans += 5*m

    three(i)
    one(i)
  else:
    three(i)
    two(i)
    one(i)
  

print(ans)
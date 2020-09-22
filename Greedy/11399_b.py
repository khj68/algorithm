n = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse=True)

times = 1
ans = 0 
for i in range(n):
    ans += times*nums[i]
    times+=1

print(ans)


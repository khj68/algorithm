first = input()
second = input()
ans = 0
for i in range(len(first)):
  if first[i] == second[i]: 
    ans += 1

print(ans)


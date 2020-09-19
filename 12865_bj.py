n, k = map(int, input().split())

# print(n,k)
weights = [0]
values = [0]
for i in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# print(weights, values)

dp = [[0]*(k+1) for _ in range(n+1)]
# print(dp)
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= weights[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
        else:
            dp[i][j] = dp[i-1][j]
# print(dp)
print(dp[n][k])
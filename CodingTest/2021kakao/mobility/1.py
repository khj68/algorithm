# 369 게임
def solution(num):
    ans = 0

    for i in range(1, num+1):
        s = str(i)
        if '3' in s or '6' in s or '9' in s:
            ans += 1
    return ans


print(solution(10))
print(solution(33))
print(solution(15))
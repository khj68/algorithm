def splitIntoTwo(arr):
    left = 0
    right = sum(arr)
    cnt = 0

    for i in range(len(arr)-1):
        left += arr[i]
        right -= arr[i]

        if (left > right):
            cnt += 1

    return cnt


print(splitIntoTwo([10, -5, 6]))
print(splitIntoTwo([10, 4, -8, 7]))
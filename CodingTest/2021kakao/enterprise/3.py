def segment(x, space):
    ans = 0
    for i in range(len(space) - x):
        m = min(space[i:i+x])
        ans = max(ans, m) 

    if not ans:
        return min(space)
    return ans


print(segment(1, [1,2,3,1,2]))
print(segment(2, [1,1,1]))
print(segment(3, [2,5,4,6,8]))
print(segment(5, [2,5,4,6,8]))
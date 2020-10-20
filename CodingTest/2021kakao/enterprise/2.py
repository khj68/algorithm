from bisect import bisect_right

def requestsServed(timestamp, top):
    timestamp.sort()
    top.sort()

    cnt = 0

    for t in top:
        idx = bisect_right(timestamp, t)
        if idx < 5:
            timestamp = timestamp[idx:]
            cnt += idx
        else:
            timestamp = timestamp[:idx-5] + timestamp[idx:]
            cnt += 5

    
    return cnt

print(requestsServed([0,1,1,2,4,5], [5]))
print(requestsServed([1, 2, 2, 3, 4, 5, 6, 6, 13, 16], [10, 15]))
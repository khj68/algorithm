from datetime import datetime
import time
import sys

def solution(n, customers):
  times = []
  kiosks = [[0,0] for _ in range(n)]
  # print(kiosks)
  for customer in customers:
    s = customer.split()
    times.append([int(time.mktime(datetime.strptime('2020 '+ s[0]+' '+ s[1], '%Y %m/%d %H:%M:%S').timetuple())), int(s[2])])
    # print(timestamp)
    
  # print('times: ', times)
  cur = times[0][0]
  for stamp, t in times:
    m_idx = 0
    m = sys.maxsize
    done = 0
    for i in range(n):
      if kiosks[i][0] <= cur:
        kiosks[i][0] = stamp + t*60
        kiosks[i][1] += 1
        done = 1
        break
      if kiosks[i][0] < m:
        m_idx = i
        m = kiosks[i][0]
    if done: continue
    kiosks[m_idx][0] = stamp + t*60
    kiosks[m_idx][1] += 1

  kiosks.sort(key = lambda x: -x[1])
  # print(kiosks)
  return kiosks[0][1]




print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))
print(solution(2, ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]))
# print(solution())
# print(solution())
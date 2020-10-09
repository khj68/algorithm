from collections import Counter
import time
def solution(k, score):
  start = time.time()
  score.sort(reverse=True)
  real = [True] * len(score)
  fakes = set()
  diff = []
  for i in range(1, len(score)):
    diff.append(score[i-1] - score[i])
  # print(diff)
  for key, val in Counter(diff).items():
    if val >= k:
      fakes.add(key)
  
  # print(fakes)
  for i in range(1, len(score)):
    if diff[i-1] in fakes:
      real[i-1] = False
      real[i] = False
  
  print('time: ', time.time() - start)
  return real.count(True)




print(solution(3, [24,22,20,10,5,3,2,1]))
print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))

import random

li = [random.randint(0, 2000000000) for _ in range(1000000)]
print(solution(3, li))
# print(solution())
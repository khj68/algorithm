import json
import requests
from collections import defaultdict
def pprint(s):
  print(json.dumps(s, indent=2, sort_keys=True))

token = '5f407e5b67aa367ef8839f1a51810792'
url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users'
n = 60
init_bikes = 3
n_trucks = 10


def start(token, problem):
  data = {'problem': problem}
  uri = url + '/start'
  return requests.post(uri, headers={'X-Auth-Token': token}, json=data).json()

def actionSome(token, actions):
  uri = url + '/some2/' + token
  return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': actions}).json()

def locations(auth_key):
  uri = url + '/locations'
  return requests.get(uri, headers={'Authorization': auth_key}).json()

def trucks(auth_key):
  uri = url + '/trucks'
  return requests.get(uri, headers={'Authorization': auth_key}).json()

def simulate(auth_key, commands):
  uri = url + '/simulate'
  return requests.put(uri, headers={'Authorization': auth_key}, json={'commands': commands}).json()

def score(auth_key):
  uri = url + '/score'
  return requests.get(uri, headers={'Authorization': auth_key}).json()

class Rental:
  def __init__(self, id):
    self.id = id
    self.bikes = 3

rental_arr = []
for i in range(n, -1, -1):
  rental_arr.append([Rental(i-1) for i in range(i, i+(n*(n-1))+1, n)])
# for i in range(n):
#   for j in range(n):
#     print(rental_arr[i][j].id)

def getLoc(id):
  r, c = id//n, n-(id%n)-1
  return r, c

def distance(a, b):
  # print(a,b)
  a_r, a_c = a//n, n-(a%n)-1
  b_r, b_c = b//n, n-(b%n)-1
  return (a_r - b_r)**2 + (a_c - b_c)**2

def move(a, b): # a->b
  command = []
  r1, c1 = getLoc(a)
  r2, c2 = getLoc(b)

  if r1 < r2: # 오른쪽으로 이동
    command.extend([2]*(r2-r1))
  else: # 왼쪽으로 이동
    command.extend([4]*(r1-r2))

  if c1 < c2: # 아래로 이동
    command.extend([3]*(c2-c1))
  else: # 위로 이동
    command.extend([1]*(c1-c2))
  
  return command

class Truck:
  def __init__(self):
    self.rentalId = 0
    self.bikes = 0
    self.moving = False
    self.dest = 0

  def action(self, maxId, minId):
    command = []

    # if self.moving:
    #   command = move(self.rentalId, self.dest)
    #   if len(command) > 10:
    #     return command[:10]
    #   elif len(command) + self.bikes > 10:
    #     return command
    #   else:
    #     self.moving = False
    #     return command + [6]*self.bikes

    command += move(self.rentalId, maxId)
    # if len(command) > 10:
    #   self.moving = True
    #   self.dest = maxId
    #   return command[:10]

    maxR, maxC = getLoc(maxId)
    # bikes = rental_arr[maxR][maxC].bikes - init_bikes
    # if bikes > 0:
    #   self.bikes += bikes
    # else: 
    if rental_arr[maxR][maxC].bikes >= 3:
      self.bikes += 1
    else:
      self.bikes += 1
    # self.bikes = min(rental_arr[maxR][maxC].bikes-2, 2)
    command += [5]*(self.bikes)
    command += move(maxId, minId)
    # if len(command) > 10:
    #   self.moving = True
    #   self.dest = minId
    #   return command[:10]
    command += [6]*self.bikes
    self.bikes = 0
    # print(command)
    return command[:10]
  


problem = 2
ret = start(token, problem)
auth_key = ret['auth_key']
truck_arr = [Truck() for _ in range(n_trucks)]

# for i in range(5):
#   for j in range(5):
#     print(arr[i][j].id)

# 처음에 각 row에 맞게 이동
# commands = []
# for i in range(n_trucks-1):
#   commands.append({'truck_id':i, 'command': [1]*(n-i-1)})
# simulate(auth_key, commands)

while True:
  worked = [False] * n_trucks
  commands = []
  locations_ret = locations(auth_key)
  trucks_ret = trucks(auth_key)
  # pprint(locations_ret)
  minDict = defaultdict(list)

  for i, d in enumerate(trucks_ret['trucks']):
    truck_arr[i].rentalId = d['location_id']
    truck_arr[i].bikes = d['loaded_bikes_count']
  
  loc = [n-1, 0]

  min_arr = []
  max_arr = defaultdict(int)
  
  for d in locations_ret['locations']:
    r, c = loc
    rental_arr[r][c].bikes = d['located_bikes_count']
    if d['located_bikes_count'] < 1:
      min_arr.append(d['id'])
    elif d['located_bikes_count'] >= 2:
      max_arr[d['id']] += d['located_bikes_count']
    if r-1 < 0:
      r = n-1
      c += 1
    else:
      r -= 1
    loc = [r, c]
  
  
  # min_arr 와 max_arr pair를 맺어줌
  for minA in min_arr:
    m = 100000
    m_i = -1
    for i, maxA in enumerate(max_arr.keys()):
      dist = distance(minA, maxA)
      minDict[minA].append((dist, maxA))
    minDict[minA].sort()
    # print('before: ',max_arr)
      # del max_arr[m_i]
    # print('after: ', max_arr)

  # for i in max_arr:
  #   print(i, end=' ')
  # print()
  # for i in min_arr:
  #   print(i, end=' ')
  # print()
  # print(pair)
  
  # pair 마다 가장 가까운 트럭 찾아서 운행
  # for i, truck in enumerate(truck_arr):
  #   if truck.moving:
  #     worked[i] = True
  #     commands.append({'truck_id': i, 'command': truck_arr[i].action(truck.rentalId, truck.dest)})
  
  for minA, maxli in minDict.items():
    m = 100000
    m_i = -1
    for maxA in maxli :
      if max_arr[maxA[1]] == 1: continue

      for i, truck in enumerate(truck_arr):
        dist = distance(maxA[1], truck.rentalId)
        if dist < m:
          if worked[i] : continue
          m_i = i
          m = dist
        worked[m_i] = True
        commands.append({'truck_id': m_i, 'command': truck_arr[m_i].action(maxA[1], minA)})
      
      break
  
  # for maxId, minId in pair:
  #   m = 100000
  #   m_i = -1
  #   for i, truck in enumerate(truck_arr):
  #     dist = distance(maxId, truck.rentalId)
  #     if dist < m:
  #       if worked[i] : continue
  #       m_i = i
  #       m = dist
  #     worked[m_i] = True
  #     commands.append({'truck_id': m_i, 'command': truck_arr[m_i].action(maxId, minId)})
  
  # for i, isWork in enumerate(worked):
  #   if isWork: continue
  #   commands.append({'truck_id': i, 'command': [0]})

  simulate_ret = simulate(auth_key, commands)
  print(simulate_ret)
  if simulate_ret['status'] == 'finished': 
    pprint(score(auth_key))
    break
import json
import requests

def pprint(s):
  print(json.dumps(s, indent=2, sort_keys=True))

token = '5f407e5b67aa367ef8839f1a51810792'
url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users'
n = 5
init_bikes = 4
n_trucks = 5


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
    self.bikes = 4

rental_arr = []
for i in range(n, -1, -1):
  rental_arr.append([Rental(i-1) for i in range(i, i+(n*(n-1))+1, n)])
# for i in range(n):
#   for j in range(n):
#     print(rental_arr[i][j].id)

def getLoc(id):
  # print(id)
  r, c = id//n, n-(id%n)-1
  return r, c

def distance(a, b):
  # print(a,b)
  a_r, a_c = a//n, n-(a%n)-1
  b_r, b_c = b//n, n-(b%n)-1
  return (a_r - b_r)**2 + (a_c - b_c)**2

def move(a, b): # a->b
  command = []
  # print(a,b)
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

  def action(self):
    commands = []
    M = -1
    m = 100
    M_i = -1
    m_i = -1
    sum_bike = 0
    m_arr = []
    for i in range(n):
      sum_bike += rental_arr[r][i].bikes
      if rental_arr[r][i].bikes > M :
        M = rental_arr[r][i].bikes
        M_i = i
      if rental_arr[r][i].bikes < m :
        m = rental_arr[r][i].bikes
        m_i = i
      if rental_arr[r][i].bikes < 2:
        m_arr.append(rental_arr[r][i].id)
    
    M_id = rental_arr[r][M_i].id
        
    
    if m > 1:
      # if r < n-1:
      #   move_bikes = m-init_bikes+1
      #   commands.extend([5]*(move_bikes))
      #   commands.append(3)
      #   commands.extend([6]*(move_bikes))
      #   commands.append(1)
      # else:
      #   move_bikes = m-init_bikes+1
      #   commands.extend([5]*(move_bikes))
      #   commands.append(3)
      #   commands.extend([6]*(move_bikes))
      #   commands.append(1)
      return [0]
      # return commands # 최소에도 자전거 충분하거나 m과 M이 같으면
    else:
      commands += move(self.rentalId, M_id)
      move_bikes = min(4, M-1)
      commands.extend([5]*(move_bikes))
      i = 0
      cur = M_id
      while move_bikes:
        commands += move(cur, m_arr[i])
        commands += [6]
        move_bikes -= 1
        i += 1
        if i == n or i == len(m_arr):
          i -= 1
        cur = m_arr[i]

      # 현재 위치에서 M_i 이동
      # if M_i == c: pass
      # elif M_i < c:  왼쪽에 있으면
      #   commands.extend([4]*(c-M_i))
      # elif M_i > c: # 오른쪽에 있으면
      #   commands.extend([2]*(M_i-c))

      # 상차
      
      # M_i에서 m_i 이동
      # if m_i < M_i: # 왼쪽에 있으면
      #   commands.extend([4]*(M_i-m_i))
      # elif m_i > M_i: # 오른쪽에 있으면
      #   commands.extend([2]*(m_i-M_i))

      # # 하차
      # commands.extend([6]*(move_bikes))
      # self.loc[1] = m_i
      return commands
    


problem = 1
ret = start(token, problem)
auth_key = ret['auth_key']
truck_arr = [Truck() for _ in range(n_trucks)]

# for i in range(5):
#   for j in range(5):
#     print(arr[i][j].id)

# 처음에 각 row에 맞게 이동
commands = []
for i in range(n_trucks-1):
  commands.append({'truck_id':i, 'command': [1]*(n-i-1)})
simulate(auth_key, commands)

while True:
  commands = []
  locations_ret = locations(auth_key)
  trucks_ret = trucks(auth_key)

  for i, d in enumerate(trucks_ret['trucks']):
    truck_arr[i].rentalId = d['location_id']
    truck_arr[i].bikes = d['loaded_bikes_count']
  
  loc = [n-1, 0]

  min_arr = []
  max_arr = []
  
  for d in locations_ret['locations']:
    r, c = loc
    rental_arr[r][c].bikes = d['located_bikes_count']
    if d['located_bikes_count'] < 2:
      min_arr.append(rental_arr[r][c])
    elif d['located_bikes_count'] > 2:
      max_arr.append(rental_arr[r][c])
    if r-1 < 0:
      r = n-1
      c += 1
    else:
      r -= 1
    loc = [r, c]
  
  pair = []
  # min_arr 와 max_arr pair를 맺어줌
  # for minA in min_arr:
  #   m = 100000
  #   m_i = -1
  #   for i, maxA in enumerate(max_arr):
  #     dist = distance(minA, maxA)
  #     if dist < m:
  #       m_i = i 
  #       m = dist
  #   pair.append((maxA.id, minA.id))
  #   del max_arr[m_i]
  # print(pair)
  for i, truck in enumerate(truck_arr):
    command = truck.action()
    # print(command)
    commands.append({'truck_id':i, 'command':command})
  
  simulate_ret = simulate(auth_key, commands)
  print(simulate_ret)
  if simulate_ret['status'] == 'finished': 
    pprint(score(auth_key))
    break
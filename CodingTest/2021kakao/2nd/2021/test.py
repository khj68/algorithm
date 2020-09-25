import json
import requests

def pprint(s):
  print(json.dumps(s, indent=2, sort_keys=True))

url = 'https://httpbin.org/get'

r = requests.get(url)

pprint(r.json())
pprint(r.json()['origin'])

def start(user, problem, count):
  uri = url + '/start/' + user + '/' + str(problem) + '/' + str(count)
  return requests.post(uri).json()

def postSome(some):
  uri = url + '/some/' + some
  return requests.post(uri).json()

def postSome2(token):
  uri = url + '/some2/' + token
  return requests.post(uri, headers={'X-Auth-Token': token}).json()

def actionSome(token, actions):
  uri = url + '/some2/' + token
  return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': actions}).json()

def getSome(some):
  uri = url + '/some/' + some
  return requests.get(uri).json()

def getSome2(some, params):
  uri = url + '/some/' + some
  return requests.get(uri, params=params).json()

def oncalls(token):
  uri = url + '/oncalls'
  return requests.get(uri, headers={'X-Auth-Token': token}).json()

user = 'jun'
problem = 0
count = 0

ret = start(user, problem, count)
token = ret['token']
print('Token for %s is %s' % (user, token))
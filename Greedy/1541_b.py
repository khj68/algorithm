import re

s = input()
s = re.split(r'(-|\+)', s)
flag = False
# print(s)
cur = 0 
for c in s:
    if c == '-':
        flag = True
        continue
    
    if c.isdigit():
        if flag:
            cur -= int(c)
        else:
            cur += int(c)
print(cur)

import math
import time
li = [1, 2, 3, 4, 5]
res = math.prod(li)
print(res)
# 2
s = 'aaa'
upper = sum(1 for i in s if i.isupper())
lower = sum(1 for i in s if i.islower())
# 3
print(s == s[::-1])
# 4
a, b = 25100, 200
time.sleep(200 / 1000)
print(f'Square root of {a} after {b} miliseconds is {math.sqrt(a)}')
# 5
tuple1 = (True, True, False, False)
print(all(tuple1))
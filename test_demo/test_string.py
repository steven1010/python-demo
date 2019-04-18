# s = 'helloworld'
# print(s[:3])
# print(s[:-1])
# print(s[1:])
# print(s[:])

# l=[123,'simple',456]
# print(l[0:])
from functools import reduce

L1 = list(map(lambda x:x%2 ==0,range(1,15)))
L2 = list(filter(lambda x:x%2 ==0,range(1,15)))
L3 = list(map(lambda x:x*x,range(1,15)))
L4 = reduce(lambda x,y: x+y,[1,2,3,4])
L5 = sum(range(1,20))

print('L1 is : {} '.format(L1))
print('L2 is : {}'.format(L2))
print('L3 is : {}'.format(L3))
print('L4 is : {}'.format(L4))
print('L5 is : {}'.format(L5))


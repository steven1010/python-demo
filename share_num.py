#Number
#int、float、bool、complex（复数）
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
#isinstance 来判断
print(isinstance(a, int))

#数字运算

# 加法
s = 5 + 4
print(s)

#减法
p = 4.3 - 2
print(p)

#乘法
m = 2*5
print(m)
#除法
r = 8/4 #得到一个浮点数
print('得到一个浮点数 {}'.format(r))
g = 9//4
print('得到一个整数 {}'.format(g))

#取余
t = 17%3
print('17 模 3 得 {}'.format(t))

#乘方
p = 2**5
print('2 的 5 次方是 {}'.format(p))


#复数complex(a,b) 或a + bj ab都是浮点型

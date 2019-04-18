# coding:utf-8
import math

# 函数赋值给变量
fun = math.sqrt
print(fun(25))


# 将函数作为参数
def fun_add(x, y, f):
    return f(x) + f(y)


print(fun_add(4, 25, fun))

print(fun_add(4, -25, abs))
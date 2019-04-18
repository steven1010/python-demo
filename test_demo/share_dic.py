# coding:utf-8
#字典推导式 (使用一句表达式构造一个新列表，可包含过滤、转换等操作)

#将0~9的数字顺序做key，倒序做value

range(10)
#倒序
reversed(range(10))

print(list(enumerate(reversed(range(10)))))
# coding:utf-8
# 集合推导式 (使用一句表达式构造一个新列表，可包含过滤、转换等操作。)

# 0~999内能被2整除的数
result = []
for i in range(0, 1000):
    if i % 2 == 0:
        result.append(i)

print(result)

# result = [i for i in range(1000) if i % 2 == 0]
# print(help(result))

# 字符串列表
str_list = ['Welcom', 'to', 'Learning', 'Python', 'Data', 'Analysis', 'Course']

# result3 = []
# result3 = [x for x in str_list]
#
# result3 = [x for x in str_list if len(x)>4]

result3 = [x.upper() for x in str_list if len(x) > 4]

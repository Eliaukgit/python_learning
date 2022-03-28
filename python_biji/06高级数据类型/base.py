# # 公共方法
# # 1.获取数据长度
# name = "小弟弟"
# print(len(name))
#
# nikename = "xiaodidi"
# length = len(nikename)
# print(length)
#
# # 2.索引，获取字符串中某个字符串的值
# foods = "玉米、包子、粥"
# print(foods[0]) # 玉 变量名 + [] + [0]下标 = 索引的方法
# print(foods[1]) # 米
# print(foods[2]) # 、
# print(foods[3]) # 包
# print(foods[4]) # 子
# print(foods[-1]) # 取最后一位
# print(foods[-3]) #  子 取倒数第三位
# print(foods[len(foods)-1]) # 粥  索引中计算长度取最后一位
#
# # 案例 循环字符串所有的字符
# content = "长江以北"
# index = 0 # 索引
# while index < len(content): # content len能够直接打印字符串的长度 0 < 4
#     char = content[index] #index 作为索引条件 content[0] [1] [2] [3]
#     print(char)
#     index = index + 1 # 计数器控制循环

# 逆序打印
content = "长江以北"
index = -1 # 索引
while index >= -len(content): # content len能够直接打印字符串的长度 -1 >= -4
    char = content[index] #index 作为索引条件 content[-1] [-2] [-3] [-4]
    print(char)
    index = index - 1 # 计数器控制循环

num = -1
while num > -2:
    print("你好")
    num -= 1



# 获取字符串中n个连续的字符的值
name = "你是风儿我是沙"
print(len(name))

n3 = name[1:3]
print(n3) # 是风  1是索引  取2到3的值

# [start,stop,step] # 开始 结束 歩长
# 开始：当以字符串的左端（字符串的开头）为起点时，索引是从0开始计数，第一个1字符为0，第二个字符为1，以此类推。。。
# 结束：当以字符串的右端开始（字符串的末尾）为起点时，索引是从-1开始计数，依次为-1、-2、-3。。。
# 步长：默认为1，2.跨过几位数取一位数

# 取到结尾的前一位
int1 = 1,2,3,4,5,6,
n3 = int1[0:6:2]
print(n3) # (1,3,5)  跳几位取几位

name = "你是风儿我是沙,缠缠绵绵到天涯"
n3 = name[0:5:3]
print(n3) # 你儿
print(name[1:5]) # 是风儿我
print(name[0:20]) # 如果取值范围大于实际则全部取出并且不会报错

print(len(name)-1) # 14
print(name[len(name)-1]) # 涯


print(name[0:])
print(name[0::]) # 默认截取全部的数据 从左边开始，可以是无线数

print(name[:-1]) # 你是风儿我是沙,缠缠绵绵到天  左闭右开

print(name[-1:]) # 涯

print(name[-2:-1]) # 天

print(name[0:len(name)]) # 你是风儿我是沙,缠缠绵绵到天涯
print(name[len(name):-2]) # 不适用
# for循环
# for i(变量) in 可迭代对象: iterable 可以被循环打印的对象
content = "三分天注定，七分靠滤镜"
int1 = 10
# for i in int1:
#     print(i) # TypeError: 'int' object is not iterable  整数不是可迭代对象

for x in content: # 相当于把content赋值给i
    print(x)

# 案例 判断用户输入的值中有多少个字符“a”（不区分A，a）
total_count = 0
"""
思路:
1.用户输入的值：if\input
content = input("请输入内容：")
2.有多少个字符“a”
if content == "A"
3.（不区分大小写）
.upper()
"""
num = 0
content = input("请输入内容：")
for i in content:
    print(i)
    if i.upper() == "A":
        print("已经找到了")
        num += 1
        print(num)
message = "你输入的内容中A/a一共有{}个".format(num)
print(message)

# 案例:break continue
data = "像我这么优秀的人，本该灿烂过一生"
for item in data:
    print(item)
    if item == "人":
        break  # 到人后直接退出

data = "像我这么优秀的人，本该灿烂过一生"
for item in data:
    if item == "人":
        print("进入if判断")
        continue  # 使用continue跳过 人
    print(item) # 像我这么优秀的进入if判断，本该灿烂过一生
a = "你"
b = "好"
print(a + b) #拼接

# 字符串拼接(join) 值的中间部分 得到一个新的字符串
data = "好的"
result = "ok".join(data)
print(result) # 好ok的

data = ["人间","烟火"] # join是字符串独有的方法
result = "的".join(data)
print(result) # 人间的烟火

data = ["汤圆","饺子"]
result = "".join(data)
print(type(data)) # <class 'list'>
print(type(result)) # <class 'str'>   "".join()完成数据类型的转换，转换成字符串
print(result) # 汤圆饺子

# 格式化字符串
name = "{}喜欢玩水".format("郭家萁")
a = name + "并且喜欢吃" + result
print(name) # 郭家萁喜欢玩水
print(a) # 郭家萁喜欢玩水并且喜欢吃汤圆饺子

data = "{}和{}的职业有法师、刺客......"
result = data.format("英雄联盟","王者荣耀")  # 如果有多个同类别插入，可以多加几个中括号
print(result)

data = "英雄联盟和王者荣耀的职业有{0}、{1}、{2}......"
result = data.format("射手","战士","辅助")  # 传多传少都会报错，一个萝卜一个坑
print(result)


# 关键字传参
data = "英雄联盟和王者荣耀的职业有{h0}、{h1}、{h2}......"
result = data.format(h1="射手",h0="战士",h2="辅助")  # 传多传少都会报错，一个萝卜一个坑  用参数传可以不考虑顺序
print(result)

# 数字格式化
print("{:.2f}".format(3.1415926))  # 3.14   .2f 保留两位小数 .3f 三位
print("{:0>2d}".format(5))  # 05    数字补任意数（1-9） 填充左边
print("{:2>3d}".format(5)) # 225 三位数字
#print("{:12>5d}".format(5)) # 报错  12125 超出范围
# 右边补充只需将>改为<

# 左对齐 右对齐 中间对齐
print("{:>10s}".format("ni")) # d是填充数字  s是填充字符串 默认为10
print("{:<10s}".format("hao")) # 左对齐
print("{:^10s}".format("呀")) # 中间对齐

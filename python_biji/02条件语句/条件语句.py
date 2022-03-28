# input("请输入用户名:")
# 执行input，在控制台任意输入，输入之后点击回车
# 之后会将输入的内容赋值给name变量，name就代指我们输入的内容
# name = input("请输入用户名：")
# print(name)

# 输出name变量代指的值
# print(type(name)) #<class'str'>

# 案例：提示输入内容,然后在姓名后面拼接一个别名，提示输入姓名，打印结果
# name = input("请输入姓名：")
# text = name + "帅哥"
# print(text)

# 案例：提示输入姓名 位置 行为 然后打印
# name = input("请输入姓名：")
# address = input("请输入位置：")
# action = input("请输入行为：")
#
# data = name + "在" + address + action
# print(data)

# 案例：提示用户输入数字，计算两个数的和
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
result = int(num1) + int(num2)  #要转换为整型来相加，因为input输入的是字符串
print(result)
"""
判断条件 如果成立，如果不成立
if 条件：
    条件成立执行if的代码

else：
    条件不成立，则执行else代码

# 如果条件成立则可以把else省去，只有：
if 条件：
    条件成立，则执行if代码
if和else语句下的代码要有相同的缩进 四个空格键 即一个tab键
"""
#
# print("开始")
# if 1 < 2: #True
#     print("条件成立，执行代码")
# if 5 == 5:
#     print("妙啊")
# else:
#     print("竟然不相等")
# print("结束")


# 案例 5 == "5" ?
# print("开始")
# if 5 == "5":
#     print("整数5等于字符串5")
# else:
#     print("整数5不等于字符串5") #False
# print("结束")
#
# # 案例
# num = 10
# if num > 9:
#     print("num变量大于9")
# else:
#     print("num变量小于9")


# 案例
# username = input("请输入用户名：")
# password = input("请输入密码：")
# # 如果同时成立，if才成立
# if username == "shinning" and password == "123456":
#     print("登陆成功！")
# else:
#     print("登陆失败...")

# 案例
username = "shinning"
if username == "shinning" or username == "jiuge":
    print("vip用户！")
else:
    print("普通用户...")


# 案例
# 通过余数奇偶数
num = 19
if 19 % 2 == 1 :
    print("19是奇数")
else:
    print("19是偶数")

# 案例
print("开始")
if 5 == 5:
    print("5等于5")
print("结束...")
"""
如果判断逻辑中有多个条件，分别对应多个操作，可以使用if  elif实现
if 条件A：

elif  条件B：

elif  条件C：

....

else：
    以上条件都不成立，则执行当前代码(如果没有功能，可以把else省略)
"""

# 用户输入数字，判断等于5，如果大于6则输入太大了，小于6则输入太小了，等于6则提示刚刚好
num = input("请输入数字：")
data = int(num)
if data > 6:
    print("输入的数字太大了")
elif data < 6:
    print("太小了")
else:
    print("刚刚好")
"""
if 条件A:
    if 条件 b:
        写代码
    else:
        写代码
elif 条件 c:
    写代码
else:
    if 条件d：
        写代码

"""

# 模拟10086客服提醒
print("欢迎致电10086，我们提供了如下的服务：1.话费相关；2.业务办理；3.人工服务")
number = int(input("请选择要咨询的服务序号："))
if number == 1:
    cost = int(input("查询话费请按1，交话费请按2："))
    if cost == 1:
        print("话费剩余10000！")
    elif cost == 2:
        print("缴纳话费1000元！")
    else:
        print("输入错误！")
elif number == 2:
    cost = int(input("宽带业务请按1,协议款余额请按2；"))
    if cost == 1:
        print("已成功为你安装宽带！")
    elif cost == 2:
        print("协议款余额为0！")
    else:
        print("输入错误！")
elif number == 3:
    print("007为您服务！")
else:
    print("序号输入错误，没有相关业务！")
# bool 非零即一
# True  1
# False 0

#判断 1 大于 2 是True/False ?
print(1 > 2)

# = 赋值
# == 判断
# 判断66 等于 99 ？
print(66 == 99) #False

# 判断字符串 "你" == “好” ？
print("你" == "好") # False
print("你" == "你") # True 通过进制来判断结果是否相等

# 判断 1 < 7
print(1 < 7)

# 字符串"666" 等于 666 ？
print("666" == 666) # False
a = 10
b = "20"
print(a * b)

str1 = "乔碧萝"
#print(10*str1)#字符串只能和整型相乘
#print(b * str1)#字符串和字符串之间不能相乘


#加法 +
#int1 = 1
str1 = "乔碧萝"
#print(int1 + str1)#整型和字符串不能相加

int2 = "1"
print(int2 + str1)#字符串与字符串相加会拼接
print("金角" + "你是大王八")#也可以直接在print中拼接字符串
# 想转换为什么类型就用哪个
# int()
# str()
# bool()

# 转换为整型
str1 = "666"
# print(int(str1)) #临时转化
# print(type(str1)) #<class 'str'>
str2 = int(str1) #永久转换
print(type(str2))

str3 = 222
print(str2 + str3)
# str3 = "q好的"
# print(int(str3)) #汉字不能转换为整型

# 布尔值转换为整型
# t = True
# f = False
# print(int(t)) # 1
# print(int(f)) # 0



#转换为字符串
#str()
print(str(666) + str(999)) # 字符串相加得到拼接

# 布尔值转换为字符串
a = True
b = False
print(str(True) + str(False))
print(True + False) # 1

# 转换为布尔值

# 整型转换为bool值
print(bool(1)) # True
print(bool(-100)) # True

# 字符串转换为bool值
print(bool("你好")) # True
print(bool("")) # False

# 其他类型转换为bool值时，空字符串和0结果为False，其他均为True

1.猜年龄游戏
print("游戏开始！")
age = int(input("请输入您猜测的年龄："))
num = 1
flag = True
while flag:
    # if age == 18 and num <= 3:
    #     print("恭喜您答对啦！")
    #     flag = False
    if num < 3:
        if age == 18:
            print("恭喜您答对啦！")
            flag = False
            continue
        else:
            if num < 3:
                print("答错啦！")
                num += 1
                age = int(input("请输入您猜测的年龄："))
                continue
    elif num == 3 and age == 18:
        print("恭喜您答对啦！")
        flag = False
    else:
        break
print("结束")

2.猜年龄游戏升级版
print("开始游戏！")
age = int(input("请输入您猜测的年龄："))
again = "游戏机会用完啦！"
flag = True
num = 1
while flag:
    if num <= 2:
        if age == 18:
            print("猜对啦！")
            break
        else:
            print("猜错啦！")
            age = int(input("请输入您猜测的年龄："))
            num += 1
        continue
    elif num == 3:
        if num == 3 and age == 18:
            print("猜对啦!")
            num += 1
            continue
    else:
        print("",again)
        again = input("是否继续进行游戏：Y or N")
        if Y:
            num = 1
        else:
            break
print("游戏结束！")


# 用户登陆系统
name = input("请输入用户名：")
password = input("请输入登录密码：")
num = 3
n = 1
flag = True
while flag:
    if num > 1:
        if name == "heihei" and password == "123":
            print("登录成功！")
            break
        else:
            print("输入错误，请重新输入！")
            num = (3 - n)
            n += 1
            print("还有" + "num" + "次机会！",num)
            name = input("请输入用户名：")
            password = input("请输入密码：")
        continue
    else:
        if name == "heihei" and password == "123":
            print("登陆成功！")
        else:
            print("登陆失败！")
        break


print("开始游戏")
num = 1
while True:
    age = int(input("请输入你猜测的年龄:"))
    if age == 18:
        print("猜对了")
        break
    else:
        print("猜错了")
    if num % 3 == 0:
        f = input('是否继续猜测:Y/N:')
        if f == 'Y' or f == 'y':
            continue
        else:
            break
    num += 1
print('游戏结束')


猜数字游戏升级版
print("游戏开始")
num = 1
while True:
    age = int(input("请输入您猜测的年龄："))
    if age == 18 :
        print("猜对了")
        break
    else:
        print("猜错了")
    if num % 3 == 0:
        f = input("是否继续猜测 Y/N:")
        if f == 'Y' or f == 'y':
            continue
        else:
            break
    num += 1
print("游戏结束")

逻辑运算符 or 如果两个值都为True 返回左边字符
print(8 or 3) # 8
print(8 or 0) # 8 如果有一个为假 同样返回左边的整数
print(0 or 8) # 8 如果有一个为假 左边为假优先返回真

and
print(1 and 3) # 3均为真 返回右边的整数
print(0 and 1) # 0 两个条件必须成立 判断才会成立 如果有一个为假 判断为假
print(2 and 0)
print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # True
print(not 2 > 1 and 3 < 4 or 4 > 5 and  2 > 1 and 9 > 8 or 7 < 6) # False
print(8 or 3 and 4 or 2 and 0 or 9 and 7)
print(0 or 2 and 3 and 4 or 6 and 0 or 3)
print(6 or 2 > 1)
print(6 or 2 > 1) # 6 or True
print(3 or 2 > 1) # True
print(0 or 5 < 4) # False or  False   # False
print(5 < 4 or 3) # False
print(2 > 1 or 6) # True or True
print(3 and 2 > 1) # True 3 and True
print(0 and 3 > 1) # 0 and True     # 0
print(2 > 1 and 3) # False
print(3 > 1 and 0) # True and 0   # 0
print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2) # 2
判断符优先级大于逻辑运算符优先级

"""优先级
** 指数
~ + - 按位翻转 一元加法和减法
* / % // 乘 除 取模 取整
>> << 右移运算符 左移运算符
& 位 “AND”
^|位运算符
< > <= >= 比较优先级
== ！= 等于 不等于运算符
= += -+ /= %= 赋值运算符
is ,is not 身份运算符
in , not in 成员运算符
not and or 逻辑运算符
"""

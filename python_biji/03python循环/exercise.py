print("文能提笔安天下，")
print("武能上马定乾坤。")
print("心存谋略何人胜，")
print("古今英雄唯是君。")

name = "xiangxue"
_ = 'xiangxue'
_9 = 'xiangxue'
# 9name = 'baolang' #不规范
# xiangxue* = 666 #不规范

# name = input("请输入xiangxue:")
# if name == "xiangxue":
#     print("真聪明！")
# else:
#     print("baibai")

score = int(input("请输入成绩："))
if  90 <= score <= 100:
    print("A!")
elif 80 <= score <= 89:
    print("B!")
elif 60 <= score <= 79:
    print("C!")
elif 40 <= score <= 59:
    print("D!")
elif 0 <= score <= 39:
    print("E!")
else:
    print("输入错误！")
# print("开始！")
# flag = True
# while flag :
#     num = int(input("请输入一个数字："))
#     if num > 66:
#         print("输入的数字大了！")
#         continue
#     elif num < 66:
#         print("输入的数字小了！")
#         continue
#     elif num == 66:
#         print("输入正确啦！")
#         break
#     else:
#         print("输入的数字错误啦！")
#         break
# print("结束！")

# print("开始！")
# num = 1
# flag = True
# while flag:
#     print(num)
#     if num <= 99:
#         num += 1
#         continue
#     else :
#         break
# print("结束啦！")

# print("开始！")
# num = 1
# flag = True
# while flag:
#     print(num)
#     if num < 6:
#         num += 1
#         continue
#     elif num == 6:
#         num += 2
#         continue
#     elif num < 10:
#         num += 1
#         continue
#     else:
#         print("循环结束啦！")
#         flag = False


# print("开始！")
# flag = True
# num = 1
# while flag:
#     if num % 2 == 1 and num <= 100:
#         print(num)
#         num += 2
#         continue
#     else:
#         break
# print("结束啦！")

# print("开始！")
# flag = True
# num = 2
# while flag:
#     if num % 2 == 0 and num < 100:
#         print(num)
#         num += 2
#         continue
#     else:
#         break
# print("结束啦！")

# print("开始")
# num = 1
# sum = 0
# while num <= 100:
#     sum += num
#     num += 1
#     print(sum)
# else:
#     print("结束啦！")


print("开始！")
num = 10
while 1 <= num <= 10:
    print(num)
    num -= 1
else:
    print("结束啦！")

# name = "虎"
# name = "猪"
# new_name = name
# name = "alex"
# print(name + new_name,end="")
# # 变量名指向后面的区域，前面的被当做垃圾数据被丢掉，由解释器自动回收

name = 18
age = str(name)
print(type(age))
print(age)

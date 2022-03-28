# 字符串变大写 得到一个新的字符串
# msg = "my name"
# print(msg.upper()) # MY NAME
# text = msg.upper()
# print(text)
#
# # 案例
# "8N9b"
# # 要求用户输入验证码
code = input("请输入4位验证码：")
# # print(code)
code = code.upper()
print(type(code)) # 当前出问题的代码
# 通过验证
# if code == "8N9B":
#     print("验证通过")
# else:
#     print("验证码输入错误")

# 字符串的小写方法 得到一个新的字符串
# msg = "My name"
# text = msg.lower() # 字符变小写 得到一个新的字符串
# print(text)

# 首字母大写
# text = "my name"
# text = text.title()
# print(text) # My Name

# swapcase() 大写变小写 小写变大写
code = input("请输入4位验证码：")
code = code.swapcase()
print(code)
if code == "fb87":
    print("验证通过")
else:
    print("输入错误")


# 猜年龄游戏
# 允许用户尝试3次 三次都错直接退出
# 思路:
# 已知条件1：允许用户猜3次
# 已知条件2:3次都没猜对的话，就直接退出
# 已知条件3：如果猜对了，打印恭喜并退出
# age = 18
# num = 0
# 已知条件1：允许用户猜3次
# while num < 3: # 3次
#     # 已知条件2:3次都没猜对的话，就直接退出
#     user_input = int(input("请输入您猜的年龄："))
#     if user_input == age:
#         print("猜对了")
#         break
#     elif user_input > age:
#         print("猜大了")
#     else:
#         print("猜小了")
#     num += 1
#
# # 猜年龄游戏升级版
# # 要求：用户最多尝试三次，每尝试三次后，如果还没猜对，就问用户是否继续玩
#     if num == 3:
#         user_input = input("已经错误三次是否继续：Y(继续)/N(退出):")
# # 如果输入Y就继续让其猜三次，以此重复
#         if user_input.upper() == "Y": # 不区分大小写 .upper.()
#             num = 0 # 修改了num的值 相当于清零之前的次数
#             continue
# # 如果输入N，就退出程序，如果猜对了就直接退出
#         elif user_input.upper() == "N":
#             break
# print("游戏结束")
#
#

# 判断字符串是否以xxx开头
v1 = "今天天气真不错呀"
result=  v1.startswith("今")
print(result) # 只要涉及到判断 结果都为bool值 True

# 判断字符串是否以xxx结尾
v2 = "今天天气不错"
result = v2.endswith("错")
print(result)

# 案例
address = input("请输入你的地址：")
if address.endswith("村"):
    print("农业户口")
else:
    print("非农业户口")
# str()

# strip 去除字符串  两边  的空格、换行符、制表符   得到一个新字符串
# print("     好的",end="") # \n(换行符) 去除就没有空行
ok = "\n\t好的\nhello\ngoodbye\t" # \n 换行符  \t 制表符 = 四个空格键或者一个tab键
# a = ok.strip() # 只能针对字符串进行操作
# print(a) # 去除print里的空格只能用end = ""
print(ok.strip()) # 好的后有换行符所以打印出来的结果hello在第二行 同理goodbye在第三行


# 删除左边空白字符串 lstrip()  删除右边的空白字符串rstrip()
hello = "                     d   "
print(hello.lstrip())
# print(hello.rstrip())

# replace() 替换
# a = "   a   b   "
# print(a.replace()) # 报错
# replace("旧字符串","新字符串",替换次数)
# print(a.replace("a","b",1))
#
my_demo = "花下醉-李商隐"
# my_demo1 = "寻芳不觉醉流霞，"
# my_demo2 ="倚树沉眠目已斜。"
# my_demo3 = "客散酒醒深夜后，"
# my_demo4 = "更持红烛赏残花。"
s = my_demo.replace("花下醉","唐",1) # 唐-李商隐
print(s) # 唐-李商隐
# print(s,my_demo1,my_demo2,my_demo3,my_demo4) # 唐-李商隐  替换不是永久替换


# split():按照指定字符分割字符串
my_demo3 = "客散酒醒深夜后,"
# my_demo3.split("分割字符",num) 分割字符是源字符串的子字符串 分割之后会丢掉   放什么进去就切割什么数据
print(my_demo3.split("酒",1)) # 分割后子字符串会丢失  ['客散', '醒深夜后,']

str1 = "s1\s2\s3"
print(str1.split("\\"))


print("""input""")
a = "哈哈"
b = '哈哈'
print(a,b)
print(type(a)) # 查看当前数据类型
c = "'包'治百病"
d = """
吵架都是我的错，
因为我可能打不过。

"""
print(a,b,c,d) # 空格也是字符串

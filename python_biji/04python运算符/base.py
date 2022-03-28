"""
运算符：
算术运算符：加减乘除
比较运算符：大于，小于，等于
赋值运算符： 变量赋值 =
成员运算符： 是否包含
逻辑运算符： 且或非
"""

# a = 10
# b = 20
# --a # 负负得正
# ++a # 正正得正
# print(a - b)
# print(--a)
# print(a/b)
# print(b % a)
# print(a % b) # 10
#
# num = 0
# while num <= 100:
#     if num % 2 == 0:
#         print("偶数",num)
#     else:
#          print("奇数",num)
#     num += 1 #缩进为一个tab键！

    # 计算100以内整数的和
# sum = 0
# num = 0
# while num <= 100:
#     #print(num)
#     sum += num
#     num += 2
# print(sum)

# a  **  b # a 的 b次方
# a // b 取整

# 判断运算符
"""
== 等于符号
!= 不等于
>= <=
> <
"""
# print("你" == "你") #十进制进行判断
# a = 19
# b = 13
# print(a == b)
#
# if a == b:
#     print("返回的结果是：",a == b)
# else :
#     if a <= b:
#         print("返回的结果是：",a <= b)
#     else:
#         print("输入有误！")

# = 赋值
# += 加法赋值运算  c += a 等价于 c = c + a
# a = "你"
# b = "好"
# a += b
# print(a)


#逆序
# num = 100
# sum = 0
# while num > 0:
#     print(num)
#     sum = num + sum
#     num -= 1
# print(sum)


# # 幂次方赋值运算
# a = 2
# b = 64
# a **= b
# print(a)

# 取整数辅助运算
# a //= b
# print(a)

# := 海象运算符 在表达式内部进行赋值

a = "你好"
if n := len(a): # 计算变量内的数据长度 整数除外
    print(n)
if n > 10:
    print("条件成立！")
else:
    print("条件不成立！")
    print(n)
#02成员运算符
# 测试
"""
in  判断在当前的序列是否存在，存在返回True 不存在返回False
not  ·····················存在返回False 不存在返回True

"""

a = "我爱北京天安门！"
print(a[3])  # 索引 0 1 2 3 4 5 6 7 8 9
if a[0] in a:
    print("当前字符存在！")
if "haha" in a:
    print("字符存在!")
else:
    print("当前字符不存在！")
if "我" not a:
    print(n)


while 0 < len(a):
    print(a)
    if len(a) :
        print(a)

b = [10,20,30]
if 10 in b:  # 整数不是一个迭代对象
    print(b)
if 57 not in b: # True
    print(b)
且或非
或 多个选一个 只要一个成立，条件就成立
a = 10
c = 20
d = 100
if a < c or c > d: # 必须有一个为真结果才为真  都为假结果为假
    print("成立！")
else:
    print("不成立！")

if a > c or c > d or d > a and a > c and d > a: # and 优先级高 只有均为真结果才为真
    print("成立！")
else:
    print("不成立！")

且 多个条件必须同时成立，条件才成立
a = 10
c = 20
d = 100
if a > c and c > b:
    print(a)
else:
    print(d)  # 100


非 如果条件为真，会返回假 条件为假 返回为真
a = 10
c = 20
d = 100
if not a < d and a < d: # False  反着来  and 优先级高
    print("成立！")
else:
    print("不成立！")

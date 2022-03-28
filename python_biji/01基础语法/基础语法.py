"""
变量
变量名 = 值 让变量指向某个值
"""

# 年龄等于18
age = 18

# 姓名
name = "郭家萁"

# 性别
gender = "女"

#
kekou,shupian,binggan,maipian = "可口可乐","薯片","饼干","麦片"
print(kekou)
print(shupian)
print(binggan)
print(maipian)
"""
变量名的定义
三条规范(必须遵循 否则会报错)：
变量名只能由字母,数字,下划线组成
变量名不能以数字开头
变量名不能是python内置关键字

两条建议(遵循更专业,不遵循也不报错)
下划线命名法:单词多比较长的时候,用下划线分开
first_name = ""
last_name = ""
见名知意：
#年龄
age = 18
#颜色
color = "red"
"""
#变量名只能由字母,数字,下划线组成
a1_ = 1
a_1 = 2
name_2 = "郭家萁"
#你好 = "111"
print(a1_)
print(a_1)
#print(你好)

#变量名不能以数字开头
#0 = "1"#SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?进行判断还是赋值
#print(0)


#变量名不能是python内置关键字
"""
int str bool(False True)


"""
#int(整型，不包含小数)
int666 = 666
print(int666)

#c = 2
#d = 1000
#result = c + d #result 结果
#print(result)

#print(10/2)

#2的4次方
# num = 2
# sum = 4
# result = num ** sum
# print(result)

# 取余数
print(10 % 3) # 1
print(10 % 2) # 0
#用引号括起来“ ”“ ”“”
#""双引号
#''单引号
#type()数据是什么类型
str1 = "你"
str2 = "好"
str3 = "吃"
str4 = "le"
print(type(str1))


#在整型中支持整型之间的加减乘除等等方法，但是在字符串里面只支持加,乘法
name = "xiangxue"#name 指向 "xiangxue"
name = "szzzz"#name不再指向“xiangxue”
new_name = name
name = "xx"
print(new_name)
print(name)

num = 18
#print(num)

age = str(num)#str字符串 num = 18 str方法的转换 把整数18转换成了字符串18
print(age)
print("你好 python")
print("hello���")
print("开始")
print("玉楼春.春恨")
print("无情不似多情苦，")
print("一寸还成千万缕，")
print("天涯地角有穷时，")
print("只有相思无尽处。")
print("结束")

#print("好的",end="")
#单行注释 shift+#
#多行注释 ctr + /
"""
多行注释，三引号括起来的内容解释器会自动忽略
shift + ”
"""

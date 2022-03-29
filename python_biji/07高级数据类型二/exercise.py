# 计算列表的长度并输出
# 请通过步长获取索引为偶数的所有值，并打印出获取后的列表
# 列表中追加元素”湖”,并输出添加后的列表
# 请在列表的第1个位置插入元素”上”,并输出添加后的列表
# 请修改列表第2个位置的元素为”联”,并输出修改后的列表
# 请将列表的第3个位置的值改成 “鲁智深”，并输出修改后的列表
# 请将列表 l2=[1,‘a’,3,4,‘baby’] 的每一个元素追加到列表li中，并输出添加后的列表
# 请将字符串 s = “qwert”的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# 请删除列表中的元素”西”,并输出添加后的列表
# 请删除列表中的第2个元素，并输出删除元素后的列表
# 请删除列表中的第2至第4个元素，并输出删除元素后的列表
li = ['西','湖','垂','柳','丝','柳','垂','湖','西']
print(len(li)) # 9

print(li[0:9:2]) # ['西', '垂', '丝', '垂', '西']

a = li.append("湖")
print(a) # None
li.append("湖")
print(li) # ['西', '湖', '垂', '柳', '丝', '柳', '垂', '湖', '西', '湖']

li.insert(0,"上")
print((li)) # ['上', '西', '湖', '垂', '柳', '丝', '柳', '垂', '湖', '西', '湖', '湖']

li[1] = "联"
print(li) # ['上', '联', '湖', '垂', '柳', '丝', '柳', '垂', '湖', '西', '湖', '湖']

li[2] = "鲁智深"
print((li)) # ['上', '联', '鲁智深', '垂', '柳', '丝', '柳', '垂', '湖', '西', '湖', '湖']

l2 = [1,'a',3,4,'baby']
li.extend(l2)
print(li) # ['上', '联', '鲁智深', '垂', '柳', '丝', '柳', '垂', '湖', '西', '湖', '湖', 1, 'a', 3, 4, 'baby']

s = "qwert"
li.append(s)
print(li) # ['上', '联', '鲁智深', '垂', '柳', '丝', '柳', '垂', '湖', '西', '湖', '湖', 1, 'a', 3, 4, 'baby', 'qwert']

li = ['西','湖','垂','柳','丝','柳','垂','湖','西']
del li[0]
del li[-1]
print(li) # ['湖', '垂', '柳', '丝', '柳', '垂', '湖']

li = ['西','湖','垂','柳','丝','柳','垂','湖','西']
del li[1]
print(li) # ['西', '垂', '柳', '丝', '柳', '垂', '湖', '西']

li = ['西','湖','垂','柳','丝','柳','垂','湖','西']
print(li)
del li[1:4]
print(li) # ['西', '丝', '柳', '垂', '湖', '西']


# 二:
li = [1,3,2,'a',4,'b',5,'c']
print(li[0:3]) # [1, 3, 2]

li = [1,3,2,'a',4,'b',5,'c']
print(li[3:6]) # ['a', 4, 'b']

li = [1,3,2,'a',4,'b',5,'c']
print(li[0:7:2]) # [1, 2, 4, 5]

li = [1,3,2,'a',4,'b',5,'c']
print(li[1:6:2]) # [3, 'a', 'b']

li = [1,3,2,'a',4,'b',5,'c']
print(li[1:8:2]) # [3, 'a', 'b', 'c']

li = [1,3,2,'a',4,'b',5,'c']
print(li[-1]) # c

li = [1,3,2,'a',4,'b',5,'c']
print(li[-3:-8:-2]) # ['b', 'a', 3]


# 三:
lis = [2,3,'k',['qwe',20,['tt',3,'1']],'ab','adv']
a = lis[2].upper()
lis[2] = a
print(lis) # [2, 3, 'K', ['qwe', 20, ['tt', 3, '1']], 'ab', 'adv']

lis[1] = "3"
lis[3][2][1] = "3"
print(lis) # [2, '3', 'K', ['qwe', 20, ['tt', '3', '1']], 'ab', 'adv']

lis[3][2][0] = 101
print(lis) # [2, '3', 'K', ['qwe', 20, [101, '3', '1']], 'ab', 'adv']

lis[3].insert(0,'火车头')
print(lis) # [2, '3', 'K', ['火车头', 'qwe', 20, [101, '3', '1']], 'ab', 'adv']


# 四:
users = ['高圆圆','赵又廷','秦霄贤']
num = 0
while num < 3:
    print(num,users[num])
    num += 1 # 0 高圆圆 1 赵又廷 2 秦霄贤

users = ['高圆圆','赵又廷','秦霄贤']
num = 1
while num < 4:
    if num == 1:
        print(num,users[0])
    elif num != 1:
        print(num,users[num-1])
    else:
        break
    num += 1  # 1 高圆圆 2 赵又廷 3 秦霄贤


# 六:
googs = ['汽车','飞机','火箭']
print("您有以下商品可供选择 0:汽车 1:飞机 2:火箭")
user_input = int(input("请选择你需要的商品序号："))
if user_input == 0:
    print("您选择的商品是" + googs[0])
elif user_input == 1:
    print("您选择的商品是" + googs[1])
elif user_input == 2:
    print("您选择的商品是" + googs[2])
else:
    print("您选择的商品暂时没有")


# 七:
data = "天{}天{}开{}心"
li = data.format("_","_","_")
print(li)

# 八:
data = []
for i in range(100):
    if i == 0:
        continue
    elif i % 2 == 0:
        data.append(i)
print(data)

# 九
data = []
for i in range(50):
    if i == 0:
        continue
    elif i % 3 == 0:
        data.append(i)
print(data)

# 十
data = []
for i in range(50):
    if i == 0:
        continue
    elif i % 3 == 0:
        data.append(i)
data.reverse()
print(data)

# 十一
li = ['西 ',' 湖','垂 ',' 柳',' 丝',' 柳','垂','湖','西']
data = []
for i in li:
    a = i.strip()
    data.append(a)
print(data)

# 作业二
# 3.
li = ["paragreaph",[11,22,(88,99,100,),33],"Zsir", ("九天", "wangzi",), "wenzhou"]
li[0] = "sentence"
print(li)

# 4.
li = ["paragreaph",[11,22,(88,99,100,),33],"Zsir", ("九天", "wangzi",), "wenzhou"]
li[3] = ['jiutian','王子']
print(li)

# 5.
li = ["paragreaph",[11,22,(88,99,100,),33],"Zsir", ("九天", "wangzi",), "wenzhou"]
li[1][2] =  (87,99,100)
print(li)

# 6.
li = ["paragreaph",[11,22,(88,99,100,),33],"Zsir", ("九天", "wangzi",), "wenzhou"]
del li[2]
li[0] = "张sir"
print((li))

# 练习三
# 1.
li = ["好好", "学习", "天天", "向上", "加油"]
for i in li:
    print((i))

# 2.
data = []
for i in range(100):
    if i % 2 == 0:
        data.append(i)
print(data)

# 3.
data = []
for i in range(50):
    if i % 3 == 0:
        data.append(i)
print(data)

# 4.
data = []
for i in range(1,100):
    data.append(i)
data.reverse()
print(data)

# 5.
data3 = []
data4 = []
for i in range(1,31):
    if i % 3 == 0:
        data3.append(i)
    elif i % 4 == 0:
        data4.append(i)
print(data3,data4)

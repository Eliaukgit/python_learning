# 1.追加：append()
# 在列表的末尾添加元素

data_list = []
data_list2 = []
# 1.提示用户输入用户名
user_name1 = input("请输入用户名：") # eca
print(user_name1)
# 2.提示用户输入昵称
user_name2 = input("请输入昵称：") # avc
print(user_name2)
data_list.append(user_name1)
data_list2.append(user_name2)
print(data_list,data_list2) # ['eca'] ['avc']


# 案例. 取元素保存到另一个列表
new_list = []
user_list = ["孔","雀","东","南","飞"]
# for x in 可迭代对象:
for i in user_list:
    # print(i)
    # 筛选
    if i == "孔":
        new_list.append(i)
print(new_list) # ['孔']


# 2.在实现数据存储的同时，可以按Q退出.
i = input("请输入数据，按Q退出：")
data = []
# 进入筛选，只要不等于Q，其他的数据都可以保存
for x in i:
    if x != "Q":
        data.append(x)
    elif x.upper() == "Q":
        break
print(data)


# 插入 在列表的指定索引位置 插入元素
user_list = ["李沁","迪丽热巴","赵丽颖"]
user_list.insert(0,"张雨绮") #  insert(索引位置,插入的元素) 临时的数据修改
a = user_list # 永久保存
print(user_list) # ['张雨绮', '李沁', '迪丽热巴', '赵丽颖']


# 3.扩展.extend(将一个列表中的元素添加到另一个列表)
dogs = ["秋田","杜宾","大白熊"]
cats = ["英短","美短"]
dogs.extend(cats)
print(dogs) # ['秋田', '杜宾', '大白熊', '英短', '美短']


data = []
data2 = ["大白熊","杜宾"]
data.extend((data2))
print(data) # ['大白熊', '杜宾']


#  4.remove()在原列表中根据元素进行删除
user_list = ["关晓彤","张天爱","马思纯"]
user_list.remove("马思纯")  # 只能放一个要删除的元素
print(user_list) # ['关晓彤', '张天爱'] 从左往右找到第一个元素进行删除


# 5.在源列表中根据索引弹出某个元素  从右往左进行弹出
user_list = ["席","床","屏风","镜台","桌子"]
ele = user_list.pop()
print(user_list) # ['席', '床', '屏风', '镜台']  并没有删除
print(ele) # 桌子  桌子保存在pop方法中
item = user_list.pop(1) # 根据下标位置弹出指定的值  只能是指定一个
print(user_list) # ['席', '屏风', '镜台']
print(item) # 床


# 6.清空原列表
user_list = ["席","床","屏风","镜台","桌子"]
data = user_list.clear()
print(user_list) # []
print(data) # None


# 7.反转列表
# 排序 0 - 3 升序  从小到大
# 3 - 0 降序  从大到小
xialian = ["山","东","人"]
xialian.reverse() # 反转
print(xialian) # ['人', '东', '山']
# list()数据类型转换
message = "黄山落叶松叶落黄山"
print(message) # 黄山落叶松叶落黄山
data = list(message)
print(data) # ['黄', '山', '落', '叶', '松', '叶', '落', '黄', '山']


message = "黄山落叶松叶落黄山"
print(type(message)) # <class 'str'>
data = list(message)
print(type(data)) # <class 'list'>

user_list = ["刘能","赵四","谢广坤"]
print(len(user_list)) # 3

a = 0,1,2,3
print(len(a)) # 4
b = 0
# print(len(b))  # 报错 多个可以用len() 一个不支持

user_list = ["刘能","赵四","谢广坤"]
print(user_list[0])  #   刘能   变量 + [] + 下标 list[0]
# print(user_list[3]) # 报错 索引超出范围
print(user_list[-1]) # 谢广坤


# 根据索引删除元素
user_list = ["范德彪","刘华强","尼古拉斯赵四","宋小宝","刘能"]
del user_list[1] # 写入del 要删除的变量 + [] + 下标
print(user_list) # ['范德彪', '尼古拉斯赵四', '宋小宝', '刘能']


# 根据索引替换元素
user_list = ["范德彪","刘华强","尼古拉斯赵四","宋小宝","刘能"]
user_list[0] = "王大拿"
print(user_list) # ['王大拿', '刘华强', '尼古拉斯赵四', '宋小宝', '刘能']

# 切片[start stop step] 和字符串一样
user_list = ["范德彪","刘华强","尼古拉斯赵四","宋小宝","刘能"]
print(user_list[1:4]) # ['刘华强', '尼古拉斯赵四', '宋小宝']
print(user_list[0:-1]) # ['范德彪', '刘华强', '尼古拉斯赵四', '宋小宝']
print(user_list[::]) # ['范德彪', '刘华强', '尼古拉斯赵四', '宋小宝', '刘能'] 从0开始 取到最右边的无限数
print(user_list[:-1]) # ['范德彪', '刘华强', '尼古拉斯赵四', '宋小宝']  start位置默认为0
print(user_list[0:5:2]) # ['范德彪', '尼古拉斯赵四', '刘能']


# for循环
user_list = ["范德彪","刘华强","尼古拉斯赵四","宋小宝","刘能"]
# a = [0,,1,2,3,4,5,1.5,"范德彪",False,True,[""],(),{}] 什么都可以往里面放
# for i in user_list:
for x in user_list:
    print(x) # 范德彪 刘华强 尼古拉斯赵四 宋小宝 刘能
    if x == "宋小宝":
        print(x) # 宋小宝


# 嵌套
# data = ["谢广坤",["海燕",["赵本山",["宋小宝"]]]]
data = ["谢广坤",["海燕","赵本山"],True,[11,22,33,44,55],"宋小宝"]
print(data[1][0]) # 海燕
print(data[4]) # 宋小宝

for i in data:
    print(i) # 谢广坤 ['海燕', '赵本山'] True [11, 22, 33, 44, 55] 宋小宝
print(data[3][1]) # 22
print(data[-4][-1]) # 赵本山
print(data[1][-1]) # 赵本山

data[1].append(666) # 把666添加到data[1]里面
for i in data:
    print(i) #  ...['海燕', '赵本山', 666]...
for i in data[1][0]:
    print(i) # 海  燕

data = ["谢广坤",["海燕","赵本山"],True,[11,22,33,44,55],"宋小宝"]
data[1].append(666)
data[1].reverse()
print(data) # ['谢广坤', [666, '赵本山', '海燕'], True, [11, 22, 33, 44, 55], '宋小宝']


# 定义一个列表 列表是一个有序的数据类型  可以被下标操作
user_list = ["玉米","西瓜","大头"]
age_list = [18,28,25]
print(user_list[0]) # 玉米  十进制逢十进一  计算机中是0到9

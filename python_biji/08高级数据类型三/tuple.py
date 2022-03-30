# turtle() # count index

# 类型转换
paragraph = "今天天气不错哦~"
print(type(paragraph)) # <class 'str'>
print(tuple(paragraph)) # ('今', '天', '天', '气', '不', '错', '哦', '~')

name = ['王二',18,'男']
print(tuple(name)) # ('王二', 18, '男')


# 获取长度
user_list = ('范德彪','刘华强','尼古拉斯赵四')
print(len(user_list)) # 3

# 索引
user_list = ('范德彪','刘华强','尼古拉斯赵四')
print(user_list[0]) # 范德彪

# 切片[start,stop,step]
user_list = ('范德彪','刘华强','尼古拉斯赵四')
print(user_list[::]) # ('范德彪', '刘华强', '尼古拉斯赵四')
print(user_list[0:3]) # 0 - 9 从小到大 升序    9 - 0 从大到小  降序  #('范德彪', '刘华强', '尼古拉斯赵四')
print(user_list[-1:-4:-1]) # ('尼古拉斯赵四', '刘华强', '范德彪')
print(user_list[-1:]) # ('尼古拉斯赵四',)
print(user_list[:-1]) # ('范德彪', '刘华强')
print(user_list[::-1]) # ('尼古拉斯赵四', '刘华强', '范德彪')

# for 循环
user_list = ('范德彪','刘华强','尼古拉斯赵四')
for i in user_list:# 可迭代对象  整数不能迭代
    print(i) # 范德彪 刘华强 尼古拉斯赵四


"""
goods = [
        {'name':'电脑','price':1999},
        {'name':'鼠标','price':10},
        {'name':'游艇','price':20},
        {'name':'美女','price':998},
]
要求:
1.页面显示 序号 + 商品名称 + 商品价格. 如:
    1 电脑 1999
    2 鼠标 10
    ...
2.用户输入选择的商品序号，然后打印商品名称及商品价格
3.如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4.用户输入Q或者q，退出程序。
"""

goods = (
    ['电脑',1999],
    ['鼠标',10],
    ['游艇','20'],
    ['美女',998]
)
moneys = []
# print(type(goods)) # <class 'tuple'>
num = 0
for i in goods:
    print('你当前可以选择的商品为：\n',num,i[0],i[1])
    num += 1
while True:
    user_input = input("请选择你需要购买的商品，请输入对应的序号：")
    if user_input == '0':
        print('你当前选择的商品是:',goods[0][0],'价格是:{}'.format(goods[0][1]))
        money = int(input('请输入需要支付的money:'))
        if money == 1999:
            print('支付成功')
            moneys.append(money)
            break
        elif money < 1999:
            print('你当前余额不足，请重新购买')
        elif money > 1999:
            sum = money - 1999
            print('你当前支付的余额超出,返回你的金额{}元'.format(sum))
    elif user_input == '1':
        print('你当前选择的商品是:',goods[1][0],'价格是:{}'.format(goods[1][1]))
    elif user_input == '2':
        print('你当前选择的商品是:',goods[2][0],'价格是:{}'.format(goods[2][1]))
    elif user_input.lower() == 'q':
        break
    else:
        print('你当前输入有误请重新输入。。。')
        continue
print('支付宝到账{}元'.format(moneys))


tu = ('清香闲自远','先向钗头见',('雪(1(2))后燕瑶池','人间第一枝'))
print(type(tu[0])) # <class 'str'>
print(tu[0][0]) # 清
print(tu[2][0][1]) # (

# 元组也是一个元组 和列表相似 但是元组不允许增删改 只允许查，私密性较好 常用于数据库
# tuple
tuple = ()
print(type(tuple)) # <class 'tuple'>

v1 = (11,22,33,"11",["22"],(1,))
print(v1) # (11, 22, 33)
print(type(v1)) # <class 'tuple'>
v2 = (1)
print(type(v2)) # <class 'int'>  单独存放数据的时候必须在后面添加上逗号，否则会还原本身的数据类型

# 比较 v1 = (1) 和 v2 = 1 和 v3 = (1,) 有什么区别
v1 = (1) # int 整数
v2 = 1 # int 整数
v3 = (1,) # 元组

v1 = ((1),(2),(3))  # 元组里存储整数元素
print(type((v1)))  # <class 'tuple'>  后面加了逗号后就都为元组了
v2 = ((1))
print(type(v2)) # <class 'int'>  （1）后没有逗号

v2 = ((1,),(2,),(3,))  # 元组里存储元组
print(type(v2)) # <class 'tuple'>

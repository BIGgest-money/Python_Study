# 列表

# my_list = [[1,2,3],[4,5,6]]
# print(my_list[-1][-2])
#
# print(type(my_list[-1][-2]))

# 查找某元素在列表内的下标索引

# my_list = ["it","you"]
#
# index = my_list.index("it")
# print(f"索引下标{index}")
#
# # 修改特定下标索引的值
#
# my_list[0] = "she"
# print(f"列表被修改元素值后，结果是：{my_list}")
#
# # 插入元素
#
# my_list.insert(1,"family")
# print(f"{my_list}")
#
# # 追加元素 写入尾部
# my_list.append("happiness")
# print(f"{my_list}")
#
# # 追加一批元素
# mylist = [1,5,6]
# my_list.extend(mylist)
# print(f"列表在追加后：{my_list}")

# mylist =[1,2,5,6,1,1]
# # 删除列表元素
# del mylist[-1]
# print(f"{mylist}")
#
# # 删除列表元素 取出元素
#
# element = mylist.pop(2)
# print(f"{mylist}，取出的元素是：{element}")
#
#
# # 删除某元素在列表中的第一个匹配项
# mylist.remove(1)
# print(f"{mylist}")
#
# # 清空列表
# mylist.clear()
# print(f"{mylist}")

# 统计列表内某元素的数量

# mylist1 = [1,1,1,5,6,8,1,1]
# count = mylist1.count(1)
# print(f"{count}")
#
# # 统计列表中全部的元素数量
#
# count = len(mylist1)
# print(f"{count}")


# tuple 元组 不可以修改

# 定义单个元素 后要加，

# t1 = (1, 5, 8, 9)
# index = t1.index(5)
# print(f"{index}")
#
# # count len()


# t2 = (1, 2, ["it","new"])
# print(f"t2的内容是：{t2}")
# t2[2][0]="you"
# t2[2][1]="me"
# print(f"{t2}")

# 字符串 不可修改
# name = "abcdefg"
#
# value = name.index("d")
# print(f"在字符串{name}中查找d,其起始下标是：{value}")
# # 替换字符串
# new = name.replace("e","yy")
# print(f"{name},{new}")


# 字符串的分割
# my_str = "hello my name is"
# my_str_list =  my_str.split(" ")
# print(f"{my_str_list}")

# 字符串的规整操作 去除前后空格


# 字符串去除前后空格
# my_str = "   you are my sunshine     "
# print(my_str.strip())
# my_str = "you is mine"
# new = my_str.strip("you")
# print(f"{new}")

# 序列 切片
# 对list进行切片，从1开始，4结束，步长1
# my_list = [0, 1, 2, 3, 4, 5, 6]
# result1 = my_list[1:4]
# print(f"结果是：{result1}")
#
# # 对tuple进行切片 从头开始到最后结束，步长1
# my_tuple = (0, 1, 2, 3, 4)
# result2 = my_tuple[:]
# print(f"结果是：{result2}")
#
# # 对str进行切片 从头开始 到最后结束 步长2
# my_str = "abcdefg"
# re3 = my_str[::2]
# print(f"结果是：{re3}")
# re4 = my_str[::-1]
# print(f"结果是：{re4}") # 倒序


# 序列的切片实践
# new = "you are my sunshine"
#
#
# new1 = new.split(" ")
# re = new1[::-1]
# print(f"{re}")
#
# re1 = "you,you,you"
# new3 = re1.replace(","," ")
# print(f"{new3}")


# 集合  去重 无序 不支持下标索引访问  允许修改
# my_set = {"you","me","you","we"}
# print(f"{my_set}")
#
# # 添加新元素
# my_set.add("brilliant")
# print(f"{my_set}")
#
# # 移除元素
# my_set.remove("we")
# print(f"{my_set}")
#
# # 取元素
# element = my_set.pop()
# print(f"{element},{my_set}")
#
# # 清空
# my_set.clear()
# print(f"{my_set}")
#
# # 取出2个集合的差集
# set1 = {1,2,3}
# set2 = {1,5,6}
# # set3 = set1.difference(set2)
# # print(set3)
#
# # 消除两个集合的差集
#
# # 两个集合合并
# set4 = set1.union(set2)
# print(f"{set4}")
#
# # 集合的遍历
# set5 = {1,2,3,4,5}
# for element in set5:
#     print(element, end = "")

# 信息去重
# my_list = ["you","me","no","yes","gear","flaw","no","yes"]
# my_set = set()
# for element in my_list:
#     my_set.add(element)
# print(my_set)

# 字典
# 新增元素
# my_dict = {"you":52,"me":98,"he":78}
# my_dict["we"] = 100
# print(my_dict)
# # 更新元素
# my_dict["you"] = 10
# print(my_dict)
#
# # 删除元素
# element = my_dict.pop("you")
# print(my_dict)
#
# # 清空元素
# # 获取全部的key
# print(my_dict.keys())
#
#
# # 遍历
# for key in my_dict.keys():
#     print(key)
#     print(my_dict[key])
# # 直接对字典进行for循环
# for key in my_dict:
#     print(key)
#     print(my_dict[key])
#
# my_dict = {
#
#                "wang":{"部门":"科技部",
#                 "工资":3000,
#                 "级别":1
#                 },
#                 "周":{"部门":"科技部",
#                 "工资":5000,
#                 "级别":2
#                 },
#                 "林":{"部门":"科技部",
#                 "工资":7000,
#                 "级别":3
#                 },
#                 "张":{"部门":"科技部",
#                 "工资":4000,
#                 "级别":2
#                 },
#
#
#            }
#
#
# for key in my_dict:
#     if my_dict[key]["级别"] == 1:
#       employee_dict = my_dict[key]
#       employee_dict["级别"] = 2
#       employee_dict["工资"] += 1000
#       my_dict[key] = employee_dict
#       print(my_dict)


# 容器通用排序功能 排序结果变列表
# my_list = [2,5,1,8]
# print(f"{sorted(my_list)}")
# print(f"{sorted(my_list, reverse=True)}")

#
# def test_return():
#     return 1,2,3
# x,y,z = test_return()
# print(x,y,z)
# f = open(r"D:\test.txt","r",encoding = "UTF-8")
# # print(f.read(2))
# # print(f.read())
# lines = f.readlines()
# print(lines)


# class Clock:
#     id = None
#     price = None
#
#
#     def ring(self):
#         import winsound
#         winsound.Beep(2000,3000)
#
# clock1 = Clock()
# clock1.id = "00302"
# clock1.price = 19.99
# print(f"闹钟ID：{clock1.id},价格：{clock1.price}")
# clock1.ring()

#
# class Information:
#     def __init__(self,name,age,tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
# for num in range(1,11):
#
#     Information1 = Information(input("请输入姓名："),input("请输入年龄"),input("请输入手机号："))
#     print(Information1.name)
#     print(Information1.age)
#     print(Information1.tel)


# class Phone:
#     __is_5g_enable = False
#
#
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print("5g关闭")
#
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
#
#
# phone = Phone()
# phone.call_by_5g()

# class Phone:
#     IMEI = None
#     producer = "YOUTUBE"
#
#     def call_by_4g(self):
#         print("4g通话")
# class Phone2024(Phone):
#     face_id = "10001"
#     def call_by_5g(self):
#         print("最新5g通话")
#
# phone = Phone2024()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()

#
# print(6/2)
# print(10//3)
# print("hello"*2)

# 38979s
# time = 38979
# hour = time // 3600
# minute = time % 3600 // 60
# second = time % 60
# print(f"{hour}小时{minute}分钟{second}秒")

#
# weight = float(input('请输入您的体重(kg)'))
# height = float(input('请输入您的身高(m)'))
# BMI = weight / height ** 2
# if 18.5 < BMI <24.9:
#     print('您的身高体重正常')


# 猜拳游戏
# import random
# player = int(input("请输入 (0)剪刀 (1)石头 (2)布："))
# computer = random.randint(0,2)
# print("玩家出的是", player)
# print("电脑出的是", computer)
# if((computer==1 and player == 0)or(computer==0 and player == 2)or(computer==2 and player == 1)):
#     print("loser")
# elif(computer == player):
#     print("ping")
# else:
#     print("winner")
# i=0
# result =0
# while i<100:
#     i += 1
#     result += i
# print(result)
# j=0
# while j<5:
#     j += 1
#     i=0
#     while i<j:
#         print("*", end = " ")
#         i += 1
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}\t",end=" ")
#     print()

# 百马百担

# for max in range(0,100//3+1):
#     for min in range(0,100//2+1):
#         if max*3+min*2+(100-max-min)*0.5==100:
#             print(max,min,100-max-min)
#

# 珠穆朗玛峰

# height = 0.08/1000
# count = 0
# while True:
#     height *= 2
#     count += 1
#     if height >= 8848.13:
#
#         break
#
# print(count)

# print('welcome to game'.center(50, '*'))
# print('   you   '.strip())
# print('   +++new++++'.strip('+'))

# 将列表转换成字符串
# fruits = ['apple','pear','peach','year']
# print('-'.join(fruits))


# 冒泡排序,
# my_list = [5, 6, 9, 10, 2, 4]
# length = len(my_list)
# i = 0
# while i < (length - 1):
#     n = 0
#     while n < (length - 1 - i):
#         if my_list[n] > my_list[n + 1]:
#             my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
#         n += 1
#     i += 1
#     print(my_list)

# nums = [6, 2, 3, 4, 5, 1, 0]
# nums.sort(reverse=True)
# print(nums)
#
# x = sorted(nums)
# print(nums)
# print(x)

#
# names = ['zhangsan', 'lisi', 'chris', 'jerry', 'henry']
# name = input("请输入姓名：")
# for name1 in names:
#     if name == name1:
#         print('姓名已存在')
#         break
# else:
#         names.append(name)
#         print(names)
# if name in names:
#     print("已存在")
# else:
#     names.append(name)
#     print(names)
# rooms = [['h','y'],['r','p','o','i'],['g']]
# for i,room in enumerate(rooms):
#     print(f"房间{i}里一共有{len(room)}个老师，分别是：",end = "")
#     for teacher in room:
#         print(teacher,end ="\t")
#     print()

# nums = [i for i in range(10)]
# print((nums))


# nums = []
# for i in range(10):
#     nums.append(i)
# print(nums)

# x = [i for i in range(10) if i % 2 == 0]
# print((x))
# y = [i for i in range(10) if i % 2]
# print(y)
#
# points = [(x,y) for x in range(5,9)for y in range(10,20)]
# print(points)

#
# chars = ['c', 'h', 't', 'd', 'c', 'a', 'a', 'q', 'p']
# char_count = {}
# for char in chars:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)
# if char not in char_count:
#     char_count[char] =chars.count(char)
# persons=[
#     {'name':'zhangsan','age':'18'}
#
#
# ]
# x=input('请输入您的姓名：')
# for person in persons:
#     if person['name'] ==x:
#         print('您输入的用户已存在')
#         break
# else:
#     new_person={'name':x}
#     y=int(input('请您输入您的年龄：'))
#     new_person['age']=y
#     persons.append(new_person)
#     print(persons)

#
# dict1={'a':100,'b':200,'x':500}
# # dict2={}
# # for v,k in dict1.items():
# #     dict2[k]=v
# # print(dict2)
# # dict1=dict2
#
# dict1={v:k for k,v in dict1.items()}
# print(dict1)

# 声明一个列表 存入学生信息
# 将列表按学生成绩从大到小排序

# students = [
#     {'name':'jack','age':'18','score':'56','phone':'13254876','gender':'female'},
#     {'name':'张三','age':'25','score':'98','phone':'13252876','gender':'male'},
#     {'name':'李四','age':'15','score':'92','phone':'13254856','gender':'female'},
#     {'name':'王五','age':'19','score':'60','phone':'13254878','gender':'male'},
#     {'name':'嘻嘻','age':'16','score':'23','phone':'13254876','gender':'unknown'},
#     {'name':'富翁','age':'22','score':'88','phone':'13254846','gender':'female'}
#
# ]
#
# # 统计不及格的学生的个数
# # 打印不及格学生的名字和对应的成绩
# count =0
# for student in students:
#     if student['score']<"60":
#         count+=1
#         print(f"{student['name']}不及格，分数为{student['score']}")
# # 统计未成年学生的个数
# num=0
# for minimum in students:
#     if minimum['age']<'18':
#         num+=1
# print(num)
#
# # 打印手机尾号是8的学生名字
#
# for cell in students:
#     # if cell['phone'][-1]=="8":
#     #     print(f"cell['name]")
#     if cell['phone'].endswith('8'):
#         print(f"{cell['name']}")
#
# max_score1 = students[0]['score']
# # 打印最高分和对应的学生的名字
# for max_score in students:
#     if max_score['score']>max_score1:
#         max_score1 = max_score['score']
# print(max_score1)
#
#
# # 删除性别不明的所有学生
#
# new_students = [x for x in students if x['gender']!='unknown']
# print(new_students)
# for j in range(0,len(students)-1):
#     for i in range(0,len(students)-1-j):
#      if students[i]['score']>students[i+1]['score']:
#         students[i],students[i+1]=students[i+1],students[i]
# print(students)


# 用三个元组表示三门学科的选课学生姓名
# 求选课学生总共有多少人
# 求只选了第一个学科的人的数量和对应的名字
# 求只选了一门学科的学生的数量和对应的名字
# 求只选了两门学科的学生的数量和对应的名字
# 求选了三门学生的学生的数量和对应的名字
sing = ('李白','白居易','李清照','杜甫','王昌龄','王维')
dance = ('李商隐','杜甫','白居易','李白','孟浩然','李商隐','王安石')
thrid = ('苏轼','王昌龄','岑参','刘禹锡','李清照')
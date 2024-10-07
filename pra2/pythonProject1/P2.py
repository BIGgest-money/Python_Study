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

#序列 切片
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
#
#
# 字符串拼接

from turtle import TurtleGraphicsError
from wsgiref.util import application_uri

# name = "温"
# address = "河北邯郸"
# print("我是"+ name +"我住在" + address)
# # 占位拼接
# class_num = 57
# avg_salary = 16781
# message = "python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
# print(message)
#
# name = "传智播客"
# set_up_year = 2006
# stock_price = 19.99
# message = "我是：%s，成立于：%d,我今天的股价是：%f" %(name, set_up_year, stock_price)
# print(message)
#
# # 数字精度控制 m.n%  m如果比变量本身宽度还要小 无效
# num1 = 11
# num2 = 11.345
# print("数字11宽度限制5，结果是：%5d" % num1)
# print("数字11宽度限制1，结果是：%d" % num1)
# print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
#
# # 字符串格式化 快速写法 format
# name = "传智播客"
# set_up_year = 2006
# stock_price = 19.99
# print(f"我是{name},成立于{set_up_year},股票价{stock_price}")

# name = "温"
# address = "河北邯郸"
# print("我是"+ name +"我住在" + address)
# # 占位拼接
# class_num = 57
# avg_salary = 16781
# message = "python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
# print(message)
#
# name = "传智播客"
# set_up_year = 2006
# stock_price = 19.99
# message = "我是：%s，成立于：%d,我今天的股价是：%f" %(name, set_up_year, stock_price)
# print(message)
#
# # 数字精度控制 m.n%  m如果比变量本身宽度还要小 无效
# num1 = 11
# num2 = 11.345
# print("数字11宽度限制5，结果是：%5d" % num1)
# print("数字11宽度限制1，结果是：%d" % num1)
# print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
#
# # 字符串格式化 快速写法 format
# name = "传智播客"
# set_up_year = 2006
# stock_price = 19.99
# print(f"我是{name},成立于{set_up_year},股票价{stock_price}")
#

# height = int(input("请输入你的身高（cm）:"))
# vip_level = int(input("请输入你的VIP等级（1-5）："))
# if height < 120:
#     print("身高小于120cm,可以免费。")
# elif vip_level > 3:
#     print("vip级别大于3，可以免费。")
# else:
#     print("不好意思，条件都不满足，需要买票10元")
#

#
# num = 5
# if int(input("请猜一个数字：")) == num:
#     print("恭喜第一次就猜对了")
# elif int(input("猜错了，请再输一次：")) == num:
#     print("猜对了")
# elif int(input("猜错了，最后一次机会：")) == num:
#     print("终于猜对了")
# else:
#     print("sorry,all error")


"""
 数字随机产生 范围1-10
 有三次机会猜测数字，通过三层嵌套判断实现
 每次猜不中，会提示大了或小了
"""

# import random
# num = random.randint(1,10)
#
#
# guess = int(input("输入你要猜测的数字:"))
#
# if guess == num:
#     print("恭喜，第一次猜中")
# else:
#     if guess > num:
#         print("大了")
#     else:
#         print("小了")
#     guess = int(input("再次输入你要猜测的数字："))
#
#     if guess == num:
#         print("恭喜，第二次猜中了")
#     else:
#         if guess > num:
#             print("大了")
#         else:
#             print("小了")
#         guess = int(input("第三次输入你要猜测的数字："))
#         if guess == num:
#             print("第三次猜中了")
#         else:
#             if guess > num:
#                 print("大了")
#             else:
#                 print("小了")
#             print("三次机会用完了，没有猜中")

# print("hello", end = '')
# print("world", end = '')

# \t 制表符

# 打印99乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j * i}\t", end = '')
#         j += 1
#     i += 1
#     print() # 换行

# count = 0
# name = "application"
# for x in name:
#     if x == "a":
#         count += 1
# print(f"{count}")

# 序列类型 ：字符串 列表 元组
# for i in range(1,10): # 控制行
#     for j in range(1,i+1): # 控制列
#         print(f"{j} * {i} = {j * i}\t", end = '')
#     print() #换行



# money = 10000
# for i in range(1,21):
#     import random
#     score = random.randint(1,10)
#
#
#     if score <5:
#         print(f"员工{i}绩效分{score}，不满足，不给发")
#         continue
#     if money >= 1000:
#         money -= 1000
#         print(f"员工{i},满足条件发放工资1000，公司账户余额：{money}")
#     else:
#         print("没钱了")
#         break


#
# def add(x,y):
#     result = x+y
#     print(f"{result}")
#
#
# add(2,7)

#
# money = 5000000
# name = input("请输入您的姓名：")
#
# def query(show_header):
#     if show_header:
#         print("-------查询余额--------")
#
#     print(f"{name},您好，您的余额剩余：{money}元")
#
# def saving(num):
#     global money
#     money  += num
#     print("-------存款--------")
#     print(f"{name},您好，您的卡汇入{num}元")
#     query(False)
# def get_money(num):
#     global money
#     money += num
#     print("-------取款--------")
#     print(f"{name},您好，您的卡取出{num}元")
#     query(False)
#
#
# def main():
#     print("--------主菜单---------")
#     print(f"{name},您好，欢迎")
#     print("查询余额\t\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("选择")
# while True:
#     key = main()
#     if key == "1":
#         query(True)
#         continue
#     elif key == "2":
#         num = int(input(":"))
#         saving(num)
#     elif key == "3":
#         num = int(input(":"))
#         get_money(num)
#     else:
#         print("quit")
#         break
#
#
#
#
#






# num = 5
# if int(input("请猜一个数字：")) == num:
#     print("恭喜第一次就猜对了")
# elif int(input("猜错了，请再输一次：")) == num:
#     print("猜对了")
# elif int(input("猜错了，最后一次机会：")) == num:
#     print("终于猜对了")
# else:
#     print("sorry,all error")





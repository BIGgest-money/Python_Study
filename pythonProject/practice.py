# 字符串拼接
name = "温"
address = "河北邯郸"
print("我是"+ name +"我住在" + address)
# 占位拼接
class_num = 57
avg_salary = 16781
message = "python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)

name = "传智播客"
set_up_year = 2006
stock_price = 19.99
message = "我是：%s，成立于：%d,我今天的股价是：%f" %(name, set_up_year, stock_price)
print(message)

# 数字精度控制 m.n%  m如果比变量本身宽度还要小 无效
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)

# 字符串格式化 快速写法 format
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
print(f"我是{name},成立于{set_up_year},股票价{stock_price}")

# height = int(input("请输入你的身高（cm）:"))
# vip_level = int(input("请输入你的VIP等级（1-5）："))
# if height < 120:
#     print("身高小于120cm,可以免费。")
# elif vip_level > 3:
#     print("vip级别大于3，可以免费。")
# else:
#     print("不好意思，条件都不满足，需要买票10元")
#

num = 5
if int(input("请猜一个数字：")) == num:
    print("恭喜第一次就猜对了")
elif int(input("猜错了，请再输一次：")) == num:
    print("猜对了")
elif int(input("猜错了，最后一次机会：")) == num:
    print("终于猜对了")
else:
    print("sorry,all error")

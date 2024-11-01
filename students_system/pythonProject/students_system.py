# import  pymysql
# from tkinter import *

# from tkinter import ttk
# import keyboard
# from pymysql import connect, Connect, Connection
# from select import select
# #  构建MySQL数据库的链接
# conn=pymysql.Connection(
#     host = 'localhost', # 主机名
#     port = 3306,
#     user = 'root',
#     password='123456'
#
# )
# # print(conn.get_server_info())
# # 获取游标对象
# cursor=conn.cursor()
# # 选择数据库
# conn.select_db('pyconnect')
# # 执行
# cursor.execute('create table winner(id int);')
#
# conn.close()



import  tkinter as  tk
from tkinter import messagebox
from pickle import TUPLE
from tkinter.ttk import Combobox
a1=tk.Tk()

a1.title('学生成绩管理系统')
# 获取用户分辨力率
a2:tuple=a1.maxsize()
k,g=a2
a1.geometry(f'{int(k*0.5)}x{int(g*0.5)}') #宽x高 距离左侧 距离右侧
# 设置窗口锁定缩放
a1.resizable(False,False)
# 设置窗口图标
a1.iconbitmap('OIP-C_16X16.ico')
# 设置窗口背景颜色
a1.configure(bg='white')
# 窗口透明度
a1.attributes('-alpha',1)
# 设置窗口置顶
a1.attributes('-topmost',True)
# 设置窗口关闭时执行的函数
def guan():
    d1= messagebox.askokcancel('是否关闭','确定关闭？')
    if d1:
        # 销毁窗口
        a1.destroy()
    else:
        pass


a1.protocol('WM_DELETE_WINDOW',guan)

# 标签组件
# a2=tk.Label(a1,text='学生成绩信息管理系统',font=('黑体',26),fg='blue',bg='white')

# 填充布局
# a2.pack()
# 自定义布局
# a2.place(x=250,y=10)

# 网格布局
# a2.grid(row=5,column=5)

tk.Label(a1,text='账号：  ', font=('黑体', 26),bg='white').place(x=150,y=100)
tk.Label(a1,text='密码：  ', font=('黑体', 26),bg='white').place(x=150,y=200)
s1 = tk.StringVar()
s1.set('请输入账号')

s2 = tk.StringVar()
s2.set('请输入密码')
# 输入框组件
tk.Entry(a1, textvariable=s1,width=20,font=('黑体',26)).place(x=250,y=100)
tk.Entry(a1,textvariable=s2 ,width=20,font=('黑体',26)).place(x=250,y=200)
def dl():
    print(s1.get())
    print(s2.get())
    if s1.get()!='123'or s2.get()!='123':
        # print(('账号密码错误'))
        messagebox.showerror('error', '账号密码错误')
    else:

        messagebox.showinfo('querry ok!', '登陆成功')


tk.Button(a1,command=dl,text='登录',font=('黑体',26),width=5).place(x=100,y=400)





# 开启窗口
a1.mainloop()
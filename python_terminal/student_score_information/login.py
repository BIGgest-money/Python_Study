import tkinter as tk
from tkinter import messagebox

# conn = pymysql.connect(
#     host='localhost',  # 数据库主机名
#     port=3306,  # 数据库端口号，默认为3306
#     user='root',  # 数据库用户名
#     passworld='root',  # 数据库密s\
#     autocommit=True  # 设置修改数据无需确认
# )
#
#



'''
 登录界面 
'''
class StudentGradeManagementSystem:
    def __init__(self):
        # 模拟数据库中的用户信息和成绩数据
        self.users = {
            "teacher1": {"password": "teacherpass", "role": "teacher"},
            "student1": {"password": "studentpass", "role": "student"},
            "parent1": {"password": "parentpass", "role": "parent"}
        }

        self.grades = {
            "student1": [80, 85, 90]  # 假设分别为平时成绩、期中考试成绩、期末考试成绩
        }

        # 全局变量用于存储当前登录用户信息
        self.current_user = None

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("学生成绩管理系统登录")
        # 获取用户分辨率
        resolution: tuple = self.root.maxsize()
        w, h = resolution
        self.root.geometry(f'{int(w * 0.25)}x{int(h * 0.25)}')  # 宽x高 距离左侧 距离右侧
        # 设置窗口锁定缩放
        self.root.resizable(False, False)
        # 设置窗口图标
        self.root.iconbitmap('OIP-C_16X16.ico')
        # 设置窗口背景颜色
        self.root.configure(bg='white')
        # 窗口透明度
        self.root.attributes('-alpha', 1)
        # 设置窗口置顶
        self.root.attributes('-topmost', True)

        # 设置窗口关闭时执行的函数
        def off():
            key = messagebox.askokcancel('是否关闭', '确定关闭？')
            if key:
                # 销毁窗口
                self.root.destroy()
            else:
                pass

        self.root.protocol('WM_DELETE_WINDOW', off)

        # s1 = tk.StringVar()
        # # s1.set('请输入账号')
        #
        # s2 = tk.StringVar()
        # # s2.set('请输入密码')
        # # 输入框组件
        # # 标签组件
        self.username_label1=tk.Label(self.root, text='学生成绩信息管理系统',font=('黑体',18),fg='blue',bg='white')

        # 自定义布局
        self.username_label1.place(x=100,y=5)

        self.username_label= tk.Label(self.root, text='账号：',font=('黑体',15),fg='blue',bg='white')
        self.username_label.place(x=30,y=50)

        self.username_entry = tk.Entry(self.root,width=15,font=('黑体',18))
        self.username_entry.place(x=60,y=100)
        self.password_label = tk.Label(self.root, text='密码：',font=('黑体',15),fg='blue',bg='white')

        self.password_label.place(x=30,y=100)
        self.password_entry = tk.Entry(self.root,width=15,font=('黑体',18))
        self.password_entry.place(x=90,y=100)
        self.login_button = tk.Button(self.root, text="登录", command=self.login,width=5,font=('黑体',12))

        self.login_button.place(x=50,y=200)
        self.login_button = tk.Button(self.root, text="注册", command=self.login, width=5, font=('黑体', 12))
        self.login_button.place(x=180, y=200)
        self.login_button = tk.Button(self.root, text="退出", command=self.login, width=5, font=('黑体', 12))
        self.login_button.place(x=320, y=200)
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            role = self.users[username]["role"]
            if role == "teacher":
                self.teacher_interface()
            elif role == "student":
                self.student_interface()
            elif role == "parent":
                self.parent_interface()
        else:
            messagebox.showerror("错误", "登录失败，请检查用户名和密码。")

    def teacher_interface(self):
        teacher_window = tk.Toplevel(self.root)
        teacher_window.title("教师界面")

        # 成绩录入部分
        def enter_grades():
            student_id = grade_student_id_entry.get()
            regular_grade = regular_grade_entry.get()
            midterm_grade = midterm_grade_entry.get()
            final_grade = final_grade_entry.get()

            try:
                regular_grade = float(regular_grade)
                midterm_grade = float(midterm_grade)
                final_grade = float(final_grade)

                # 这里假设将成绩存储在grades字典中，实际应用中应使用数据库
                if student_id not in self.grades:
                    self.grades[student_id] = []
                self.grades[student_id].append(regular_grade)
                self.grades[student_id].append(midterm_grade)
                self.grades[student_id].append(final_grade)
                messagebox.showinfo("成功", "成绩录入成功！")
            except ValueError:
                messagebox.showerror("错误", "成绩输入应为数字！")

        # 教师界面布局
        grade_student_id_label = tk.Label(teacher_window, text="学生学号:")
        grade_student_id_label.pack()
        grade_student_id_entry = tk.Entry(teacher_window)
        grade_student_id_entry.pack()

        regular_grade_label = tk.Label(teacher_window, text="平时成绩:")
        regular_grade_label.pack()
        regular_grade_entry = tk.Entry(teacher_window)
        regular_grade_entry.pack()

        midterm_grade_label = tk.Label(teacher_window, text="期中考试成绩:")
        midterm_grade_label.pack()
        midterm_grade_entry = tk.Entry(teacher_window)
        midterm_grade_entry.pack()

        final_grade_label = tk.Label(teacher_window, text="期末考试成绩:")
        final_grade_label.pack()
        final_grade_entry = tk.Entry(teacher_window)
        final_grade_entry.pack()

        enter_grades_button = tk.Button(teacher_window, text="录入成绩", command=enter_grades)
        enter_grades_button.pack()

    def student_interface(self):
        student_window = tk.Toplevel(self.root)
        student_window.title("学生界面")

        # 成绩查询部分
        def query_grades():
            # 这里假设从grades字典中获取成绩，实际应用中应从数据库查询
            if self.current_user in self.grades:
                messagebox.showinfo("成绩查询", f"平时成绩: {self.grades[self.current_user][0]}\n期中考试成绩: {self.grades[self.current_user][1]}\n期末考试成绩: {self.grades[self.current_user][2]}")
            else:
                messagebox.showinfo("成绩查询", "未找到你的成绩信息。")

        # 学生界面布局
        query_grades_button = tk.Button(student_window, text="查询成绩", command=query_grades)
        query_grades_button.pack()

    def parent_interface(self):
        parent_window = tk.Toplevel(self.root)
        parent_window.title("家长界面")

        # 成绩查询部分（与学生界面类似，但可能根据实际需求有所不同，这里简单示例相同功能）
        def query_child_grades():
            # 假设家长关联的学生是student1（这里可根据实际情况扩展逻辑，比如让家长选择关联的学生）
            student_id = "student1"
            if student_id in self.grades:
                messagebox.showinfo("成绩查询", f"孩子平时成绩: {self.grades[student_id][0]}\n期中考试成绩: {self.grades[student_id][1]}\n期末考试成绩: {self.grades[student_id][2]}")
            else:
                messagebox.showinfo("成绩查询", "未找到孩子的成绩信息。")

        # 家长界面布局
        query_child_grades_button = tk.Button(parent_window, text="查询孩子成绩", command=query_child_grades)
        query_child_grades_button.pack()

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
        app = StudentGradeManagementSystem()
        app.run()

# def login(self):
#     username = self.username_entry.get()
#     password = self.password_entry.get()
#
#     if username in self.users and self.users[username]["password"] == password:
#         self.current_user = username
#         role = self.users[username]["role"]
#         if role == "teacher":
#             self.teacher_interface()
#         elif role == "student":
#             self.student_interface()
#         elif role == "parent":
#             self.parent_interface()
#     else:
#         messagebox.showerror("错误", "登录失败，请检查用户名和密码。")
import tkinter as tk
from tkinter import messagebox


# 模拟数据库中的用户信息（这里简单用字典存储，实际应用中应使用数据库）
users = {}

# 全局变量用于存储当前登录用户信息
current_user = None
current_user_role = None

class StudentGradeManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("学生成绩管理系统")
        # 获取用户分辨率
        resolution: tuple = self.root.maxsize()
        w, h = resolution
        self.root.geometry(f'{int(w * 0.3)}x{int(h * 0.3)}')  # 宽x高 距离左侧 距离右侧
        # 设置窗口锁定缩放
        self.root.resizable(False, False)
        # 设置窗口图标
        self.root.iconbitmap('OIP-C_16X16.ico')
        # 设置窗口背景颜色
        self.root.configure(bg='white')
        # 窗口透明度
        self.root.attributes('-alpha', 1)
        # # 设置窗口置顶
        # self.root.attributes('-topmost', True)

        # 设置窗口关闭时执行的函数
        def off():
            key = messagebox.askokcancel('是否关闭', '确定关闭？')
            if key:
                # 销毁窗口
                self.root.destroy()
            else:
                pass

        self.root.protocol('WM_DELETE_WINDOW', off)

        # # 设置窗口大小和位置
        # window_width = 400
        # window_height = 300
        # screen_width = self.root.winfo_screenwidth()
        # screen_height = self.root.winfo_screenheight()
        # x = (screen_width - window_width) // 2
        # y = (screen_height - window_height) // 2
        # self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 登录标签和输入框
        self.username_label1 = tk.Label(self.root, text='学生成绩信息管理系统', font=('黑体', 18), fg='blue',bg='white')
        self.username_label1.place(x=100, y=5)
        self.login_label = tk.Label(self.root, text="账户：",font=('黑体',15),bg='white')
        self.login_label.place(x=50, y=50)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(x=110, y=50)
        self.login_label = tk.Label(self.root,text="密码：",font=('黑体',15),bg='white')
        self.login_label.place(x=50, y=100)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.place(x=110, y=100)

        # 注册按钮
        self.register_button = tk.Button(self.root, text="注册", command=self.register)
        self.register_button.place(x=100, y=200)

        # 登录按钮
        self.login_button = tk.Button(self.root, text="登录", command=self.login)
        self.login_button.place(x=180, y=200)

        # 退出按钮
        self.exit_button = tk.Button(self.root, text="退出", command=self.root.quit)
        self.exit_button.place(x=260, y=200)

    def register(self):
        # 注册窗口
        register_window = tk.Toplevel(self.root)
        register_window.title("注册")

        # 设置窗口大小和位置
        window_width = 300
        window_height = 200
        screen_width = register_window.winfo_screenwidth()
        screen_height = register_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        register_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 账号标签和输入框
        self.register_username_label = tk.Label(register_window, text="账号：")
        self.register_username_label.place(x=30, y=30)
        self.register_username_entry = tk.Entry(register_window)
        self.register_username_entry.place(x=80, y=30)

        # 密码标签和输入框
        self.register_password_label = tk.Label(register_window, text="密码：")
        self.register_password_label.place(x=30, y=60)
        self.register_password_entry = tk.Entry(register_window, show="*")
        self.register_password_entry.place(x=80, y=60)

        # 确认密码标签和输入框
        self.register_confirm_password_label = tk.Label(register_window, text="确认密码：")
        self.register_confirm_password_label.place(x=10, y=90)
        self.register_confirm_password_entry = tk.Entry(register_window, show="*")
        self.register_confirm_password_entry.place(x=80, y=90)

        # 注册按钮
        self.register_submit_button = tk.Button(register_window, text="注册", command=self.perform_register)
        self.register_submit_button.place(x=100, y=130)

    def perform_register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        confirm_password = self.register_confirm_password_entry.get()

        if password!= confirm_password:
            messagebox.showerror("注册失败", "两次密码不一致，请重新输入。")
            return

        if username in users:
            messagebox.showerror("注册失败", "该账号已存在，请选择其他账号。")
            return

        # 这里简单将用户信息存储在字典中，实际应用应存储到数据库
        users[username] = {"password": password, "role": "teacher"}  # 默认注册为学生角色，可根据需求扩展
        messagebox.showinfo("注册成功", "注册成功！您可以登录了。")
        self.close_register_window()

    def close_register_window(self):
        # 关闭注册窗口
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username]["password"] == password:
            global current_user, current_user_role
            current_user = username
            current_user_role = users[username]["role"]
            messagebox.showinfo("登录成功", f"欢迎，{current_user}！您的角色是{current_user_role}。")
            self.show_appropriate_interface()
        else:
            messagebox.showerror("登录失败", "用户名或密码错误，请重新输入。")

    def show_appropriate_interface(self):
        if current_user_role == "teacher":
            self.show_teacher_interface()
        elif current_user_role == "student":
            self.show_student_interface()
        elif current_user_role == "parent":
            self.show_parent_interface()



    '''
     教师界面
    '''

    def show_teacher_interface(self):
            teacher_window = tk.Toplevel(self.root)
            teacher_window.title("教师界面")

            # # 获取用户分辨率
            # resolution: tuple = self.root.maxsize()
            # w, h = resolution
            teacher_window .geometry('500x500')  # 宽x高 距离左侧 距离右侧
            # 设置窗口锁定缩放
            teacher_window.resizable(False, False)
            # 设置窗口图标
            teacher_window .iconbitmap('OIP-C_16X16.ico')
            # 设置窗口背景颜色
            teacher_window .configure(bg='white')
            # 窗口透明度
            teacher_window .attributes('-alpha', 1)
            # 查询输入框和标签
            self.query_id_label = tk.Label(teacher_window, text=" 学 号",font=('黑体',16),bg='white')
            self.query_id_label.place(x=70, y=30)
            self.query_id_entry = tk.Entry(teacher_window)
            self.query_id_entry.place(x=140, y=30)

            self.query_name_label = tk.Label(teacher_window, text=" 姓 名",font=('黑体',16),bg='white')
            self.query_name_label.place(x=70, y=60)
            self.query_name_entry = tk.Entry(teacher_window)
            self.query_name_entry.place(x=140, y=60)

            self.query_class_label = tk.Label(teacher_window, text="班 级",font=('黑体',16),bg='white')
            self.query_class_label.place(x=80, y=90)
            self.query_class_entry = tk.Entry(teacher_window)
            self.query_class_entry.place(x=150, y=90)


            def show_mess(self):
                mess_window = tk.Toplevel(teacher_window)
                mess_window.title("学生成绩管理系统")


                mess_window.geometry('500x700')  # 宽x高 距离左侧 距离右侧
                # 设置窗口锁定缩放
                mess_window.resizable(False, False)
                # 设置窗口图标
                mess_window.iconbitmap('OIP-C_16X16.ico')
                # 设置窗口背景颜色
                mess_window.configure(bg='white')
                # 窗口透明度
                mess_window.attributes('-alpha', 1)
                messagebox.showinfo('操作成功','查询成功')

                # self.mess_button = tk.Button(mess_window, text="ok", width=10, command=self.query_teacher)
                # self.mess_button.place(x=250, y=400)

            self.query_button = tk.Button(teacher_window, text="查询", width=10,command=self.query_teacher)
            self.query_button.place(x=350, y=400)
            self.query_button = tk.Button(teacher_window, text="录入", width=10,command=self.query_teacher)
            self.query_button.place(x=250, y=400)
            self.query_button = tk.Button(teacher_window, text="修改", width=10,command=self.query_teacher)
            self.query_button.place(x=150, y=400)
            self.query_button = tk.Button(teacher_window, text="删除", width=10,command=self.query_teacher)
            self.query_button.place(x=50, y=400)


            # 创建菜单
            self.menu_bar = tk.Menu(teacher_window)
            self.display_menu = tk.Menu(self.menu_bar, tearoff=0)

            # 排名菜单
            self.rank_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.rank_menu.add_command(label="升序", command=lambda: self.show_rank(True))
            self.rank_menu.add_command(label="降序", command=lambda: self.show_rank(False))
            self.menu_bar.add_cascade(label="排名", menu=self.rank_menu)

            # 学号菜单
            self.student_id_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.student_id_menu.add_command(label="升序", command=lambda: self.show_student_id(True))
            self.student_id_menu.add_command(label="降序", command=lambda: self.show_student_id(False))
            self.menu_bar.add_cascade(label="学号", menu=self.student_id_menu)

            # 姓名菜单
            self.student_name_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.student_name_menu.add_command(label="升序", command=lambda: self.show_student_name(True))
            self.student_name_menu.add_command(label="降序", command=lambda: self.show_student_name(False))
            self.menu_bar.add_cascade(label="姓名", menu=self.student_name_menu)

            # 各科成绩菜单
            self.subject_grades_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.subject_grades_menu.add_command(label="数学成绩（升序）",
                                                 command=lambda: self.show_subject_grades(True, "math"))
            self.subject_grades_menu.add_command(label="数学成绩（降序）",
                                                 command=lambda: self.show_subject_grades(False, "math"))
            self.subject_grades_menu.add_command(label="英语成绩（升序）",
                                                 command=lambda: self.show_subject_grades(True, "english"))
            self.subject_grades_menu.add_command(label="英语成绩（降序）",
                                                 command=lambda: self.show_subject_grades(False, "english"))
            self.subject_grades_menu.add_command(label="科学成绩（升序）",
                                                 command=lambda: self.show_subject_grades(True, "science"))
            self.subject_grades_menu.add_command(label="科学成绩（降序）",
                                                 command=lambda: self.show_subject_grades(False, "science"))
            self.menu_bar.add_cascade(label="各科成绩", menu=self.subject_grades_menu)


            # 总成绩菜单
            self.total_grades_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.total_grades_menu.add_command(label="总成绩（升序）", command=lambda: self.show_total_grades(True))
            self.total_grades_menu.add_command(label="总成绩（降序）", command=lambda: self.show_total_grades(False))
            self.menu_bar.add_cascade(label="总成绩", menu=self.total_grades_menu)

            teacher_window.config(menu=self.menu_bar)

            # self.menu_bar.add_cascade(label="排名", command=lambda: self.show_rank(True))
            # self.menu_bar.add_cascade(label="排名（降序）", command=lambda: self.show_rank(False))
            # self.menu_bar.add_cascade(label="学号", command=lambda: self.show_student_id(True))
            # # self.menu_bar.add_cascade(label="学号（降序）", command=lambda: self.show_student_id(False))
            # # self.menu_bar.add_cascade(label="姓名（升序）", command=lambda: self.show_student_name(True))
            # self.menu_bar.add_cascade(label="姓名", command=lambda: self.show_student_name(False))
            # # self.menu_bar.add_cascade(label="各科成绩（升序）", command=lambda: self.show_subject_grades(True))
            # self.menu_bar.add_cascade(label="各科成绩", command=lambda: self.show_subject_grades(False))
            # # self.menu_bar.add_cascade(label="总成绩（升序）", command=lambda: self.show_total_grades(True))
            # self.menu_bar.add_cascade(label="总成绩", command=lambda: self.show_total_grades(False))
            # self.menu_bar.add_cascade(label="显示", menu=self.display_menu)
            # teacher_window.config(menu=self.menu_bar)


            # 初始化显示为空
            self.show_empty_result(teacher_window)



            # # 设置窗口关闭时执行的函数
            # def off1():
            #     key = messagebox.askokcancel('是否关闭', '确定关闭？')
            #     if key:
            #         # 销毁窗口
            #         teacher_window.destroy()
            #     else:
            #         pass
            #
            # teacher_window.protocol('WM_DELETE_WINDOW', off1)
            teacher_window.destroy()
            # def show_mess(self):
            #     mess_window = tk.Toplevel(teacher_window)
            #     mess_window.title("学生成绩管理系统")
            #
            #
            #     mess_window.geometry('500x700')  # 宽x高 距离左侧 距离右侧
            #     # 设置窗口锁定缩放
            #     mess_window.resizable(False, False)
            #     # 设置窗口图标
            #     mess_window.iconbitmap('OIP-C_16X16.ico')
            #     # 设置窗口背景颜色
            #     mess_window.configure(bg='white')
            #     # 窗口透明度
            #     mess_window.attributes('-alpha', 1)
            #
            #
            #     self.mess_button = tk.Button(mess_window, text="ok", width=10, command=self.query_teacher)
            #     self.mess_button.place(x=250, y=400)


    def query_teacher(self):
            student_id = self.query_id_entry.get()
            student_name = self.query_name_entry.get()
            student_class = self.query_class_entry.get()
        #
        #     # 这里简单模拟查询逻辑，实际应从数据库查询
        #     matching_students = []
        #     for student, grades in student_grades.items():
        #         if (not student_id or student_id == grades["id"]) and \
        #                 (not student_name or student_name == grades["name"]) and \
        #                 (not student_class or student_class == grades["class"]):
        #             total_grade = sum(grades.values()) - grades["class"] - grades["name"]  # 计算总成绩，排除班级和姓名字段
        #             grades["total"] = total_grade  # 添加总成绩字段到成绩数据中
        #             matching_students.append((student, grades))
        #
        #     if matching_students:
        #         self.show_query_results(matching_students)
        #     else:
        #         messagebox.showinfo("查询结果", "未找到匹配的学生信息。")
        #
        # def show_query_results(self, students_data):
        #     # 清空之前的显示
        #     for widget in self.root.winfo_children():
        #         if isinstance(widget, tk.Label) and widget.winfo_parent() == self.root:
        #             widget.destroy()
        #
        #     for student, grades in students_data:
        #         student_info = f"学号：{student}, 姓名：{grades['name']}, 班级：{grades['class']}, 总成绩：{grades['total']}"
        #         tk.Label(self.root, text=student_info).pack()
        #         for subject, grade in grades.items():
        #             if subject in ["math", "english", "science"]:
        #                 subject_label = tk.Label(self.root, text=f"{subject}成绩：{grade}")
        #                 subject_label.pack()
        #
        # def show_empty_result(self, window):
        #     empty_label = tk.Label(window, text="暂无查询结果。")
        #     empty_label.pack()
        #
        # def show_rank(self, ascending=True):
        #     # 模拟排名逻辑，这里简单根据总成绩进行排序并在控制台输出
        #     sorted_students = sorted(student_grades.items(), key=lambda x: x[1]["total"], reverse=not ascending)
        #     print(f"排名（{'升序' if ascending else '降序'}）:")
        #     for i, (student, grades) in enumerate(sorted_students, start=1):
        #         print(f"{i}. 学号：{student}, 姓名：{grades['name']}, 总成绩：{grades['total']}")
        #
        # def show_student_id(self, ascending=True):
        #     # 模拟按学号排序逻辑，这里简单对学号进行排序并在控制台输出
        #     sorted_students = sorted(student_grades.items(), key=lambda x: x[0], reverse=not ascending)
        #     print(f"学号（{'升序' if ascending else '降序'}）:")
        #     for student, grades in sorted_students:
        #         print(f"学号：{student}, 姓名：{grades['name']}, 总成绩：{grades['total']}")
        #
        # def show_student_name(self, ascending=True):
        #     # 模拟按姓名排序逻辑，这里简单对姓名进行排序并在控制台输出
        #     sorted_students = sorted(student_grades.items(), key=lambda x: x[1]["name"], reverse=not ascending)
        #     print(f"姓名（{'升序' if ascending else '降序'}）:")
        #     for student, grades in sorted_students:
        #         print(f"学号：{student}, 姓名：{grades['name']}, 总成绩：{grades['total']}")

        # def show_subject_grades(self, ascending=True):
        #     # 模拟按各科成绩排序逻辑，这里以数学成绩为例进行排序并在控制台输出
        #     sorted_students = sorted(student_grades.items(), key=lambda x: x[1]["math"], reverse=not ascending)
        #     print(f"数学成绩（{'升序' if ascending else '降序'}）:")
        #     for student, grades in sorted_students:
        #         print(f"学号：{student}, 姓名：{grades['name']}, 数学成绩：{grades['math']}, 总成绩：{grades['total']}")

        #def show_total_grades(self, ascending=True):
            # # 模拟按总成绩排序逻辑，与show_rank类似但直接在界面显示排序后的学生信息
            # sorted_students = sorted(student_grades.items(), key=lambda x: x[1]["total"], reverse=not ascending)
            # self.show_query_results(sorted_students)



    '''
    学生界面
    '''

    def show_student_interface(self):
        student_window = tk.Toplevel(self.root)
        student_window.title("学生界面")

        # 设置窗口大小和位置
        # window_width = 1000
        # window_height = 1000
        # screen_width = self.root.winfo_screenwidth()
        # screen_height = self.root.winfo_screenheight()
        # x = (screen_width - window_width) // 2
        # y = (screen_height - window_height) // 2
        # self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # # 获取用户分辨率
        # resolution: tuple = self.student_window.maxsize()
        # w, h = resolution
        student_window.geometry('500x500')  # 宽x高 距离左侧 距离右侧
        # 设置窗口锁定缩放
        student_window.resizable(False, False)
        # 设置窗口图标
        student_window.iconbitmap('OIP-C_16X16.ico')
        # 设置窗口背景颜色
        student_window.configure(bg='white')
        # 窗口透明度
        student_window.attributes('-alpha', 1)

        # 查询输入框和标签（学生只能查询自己信息，这里假设学号固定为当前登录学生学号）
        self.query_id_label = tk.Label(student_window, text="学号：")
        self.query_id_label.place(x=30, y=30)
        self.query_id_entry = tk.Entry(student_window)
        self.query_id_entry.place(x=80, y=30)
        self.query_id_entry.insert(0, current_user)  # 自动填入当前学生学号
        self.query_id_entry.config(state='readonly')  # 设置为只读

        self.query_button = tk.Button(student_window, text="查询", command=self.query_parent)
        self.query_button.place(x=180, y=60)

        # 创建菜单（学生界面菜单，去除删除相关选项）
        self.menu_bar = tk.Menu(student_window)
        self.display_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.display_menu.add_command(label="排名（升序）", command=lambda: self.show_rank(True))
        self.display_menu.add_command(label="排名（降序）", command=lambda: self.show_rank(False))
        self.display_menu.add_command(label="学号（升序）", command=lambda: self.show_student_id(True))
        self.display_menu.add_command(label="学号（降序）", command=lambda: self.show_student_id(False))
        self.display_menu.add_command(label="姓名（升序）", command=lambda: self.show_student_name(True))
        self.display_menu.add_command(label="姓名（降序）", command=lambda: self.show_student_name(False))
        self.display_menu.add_command(label="各科成绩（升序）", command=lambda: self.show_subject_grades(True))
        self.display_menu.add_command(label="各科成绩（降序）", command=lambda: self.show_subject_grades(False))
        self.display_menu.add_command(label="总成绩（升序）", command=lambda: self.show_total_grades(True))
        self.display_menu.add_command(label="总成绩（降序）", command=lambda: self.show_total_grades(False))
        self.menu_bar.add_cascade(label="显示", menu=self.display_menu)
        student_window.config(menu=self.menu_bar)

        # 初始化显示为空
        self.show_empty_result(student_window)

    # def query_student(self):
    #     student_id = self.query_id_entry.get()

        # 这里简单模拟查询自己成绩逻辑，实际应从数据库查询

        # if student_id in student_grades:
        #
        # else:
        #     messagebox.showinfo("查询结果", "未找到自己的成绩信息。")

    def show_parent_interface(self):
        parent_window = tk.Toplevel(self.root)
        parent_window.title("家长界面")

        # 查询输入框和标签（假设家长只能查询与当前登录学生相关信息，这里学号固定为当前登录学生学号）
        self.query_id_label = tk.Label(parent_window, text="学号：")
        self.query_id_label.place(x=30, y=30)
        self.query_id_entry = tk.Entry(parent_window)
        self.query_id_entry.place(x=80, y=30)
        self.query_id_entry.insert(0, current_user)  # 自动填入当前学生学号
        self.query_id_entry.config(state=' readonly')  # 设置为只读

        self.query_button = tk.Button(parent_window, text="查询", command=self.query_parent)
        self.query_button.place(x=180, y=60)

        # 创建菜单（家长界面菜单，去除删除相关选项）
        self.menu_bar = tk.Menu(parent_window)
        self.display_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.display_menu.add_command(label="排名（升序）", command=lambda: self.show_rank(True))
        self.display_menu.add_command(label="排名（降序）", command=lambda: self.show_rank(False))
        self.display_menu.add_command(label="学号（升序）", command=lambda: self.show_student_id(True))


if __name__ == "__main__":
    app = StudentGradeManagementSystem()
    app.root.mainloop()
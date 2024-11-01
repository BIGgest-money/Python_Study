import tkinter as tk
from tkinter import messagebox
from pymysql import Connection
from ttkbootstrap import Style

# 连接到MySQL数据库
mydb =  Connection(
    host="localhost",
    user='root',
    password="123456",
    port=3306
)

mycursor = mydb.cursor()

# 检查数据库中是否存在students表，如果不存在则创建
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    student_id VARCHAR(255) UNIQUE NOT NULL,
    class VARCHAR(255) NOT NULL,
    math_grade DECIMAL(5, 2),
    english_grade DECIMAL(5, 2),
    science_grade DECIMAL(5, 2)
)
""")

# 全局变量用于存储当前登录用户信息
current_user = None
current_user_role = None

class StudentGradeManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("学生成绩管理系统")

        # 设置窗口风格
        style = Style(theme="flatly")

        # 设置窗口大小和位置
        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 登录标签和输入框
        self.login_label = tk.Label(self.root, text="登录：")
        self.login_label.pack(pady=(30, 0))
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=(10, 0))

        # 注册按钮
        self.register_button = tk.Button(self.root, text="注册", command=self.register)
        self.register_button.pack()

        # 登录按钮
        self.login_button = tk.Button(self.root, text="登录", command=self.login)
        self.login_button.pack(pady=(10, 0))

        # 退出按钮
        self.exit_button = tk.Button(self.root, text="退出", command=self.root.quit)
        self.exit_button.pack()

    def register(self):
        # 注册窗口
        register_window = tk.Toplevel(self.root)
        register_window.title("注册")

        # 设置窗口风格
        style = Style(theme="flatly")

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
        self.register_username_label.pack(pady=(30, 0))
        self.register_username_entry = tk.Entry(register_window)
        self.register_username_entry.pack()

        # 密码标签和输入框
        self.register_password_label = tk.Label(register_window, text="密码：")
        self.register_password_label.pack()
        self.register_password_entry = tk.Entry(register_window, show="*")
        self.register_password_entry.pack(pady=(10, 0))

        # 确认密码标签和输入框
        self.register_confirm_password_label = tk.Label(register_window, text="确认密码：")
        self.register_confirm_password_label.pack()
        self.register_confirm_password_entry = tk.Entry(register_window, show="*")
        self.register_confirm_password_entry.pack(pady=(10, 0))

        # 注册按钮
        self.register_submit_button = tk.Button(register_window, text="注册", command=self.perform_register)
        self.register_submit_button.pack(pady=(10, 0))

    def perform_register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        confirm_password = self.register_confirm_password_entry.get()

        if password!= confirm_password:
            messagebox.showerror("注册失败", "两次密码不一致，请重新输入。")
            return

        # 检查用户名是否已存在
        mycursor.execute("SELECT * FROM students WHERE student_id = %s", (username,))
        if mycursor.fetchone():
            messagebox.showerror("注册失败", "该账号已存在，请选择其他账号。")
            return

        # 将新用户信息插入数据库
        mycursor.execute("INSERT INTO students (student_id, name, password) VALUES (%s, %s, %s)", (username, '默认姓名', password))
        mydb.commit()

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

        # 验证登录信息
        mycursor.execute("SELECT * FROM students WHERE student_id = %s AND password = %s", (username, password))
        result = mycursor.fetchone()
        if result:
            global current_user, current_user_role
            current_user = username
            current_user_role = "student"  # 这里假设所有注册用户都是学生角色，可根据实际需求扩展
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

    def show_teacher_interface(self):
        teacher_window = tk.Toplevel(self.root)
        teacher_window.title("教师界面")

        # 设置窗口风格
        style = Style(theme="flatly")

        # 查询输入框和标签
        self.query_id_label = tk.Label(teacher_window, text="学号：")
        self.query_id_label.pack(pady=(30, 0))
        self.query_id_entry = tk.Entry(teacher_window)
        self.query_id_entry.pack()

        self.query_name_label = tk.Label(teacher_window, text="姓名：")
        self.query_name_label.pack()
        self.query_name_entry = tk.Entry(teacher_window)
        self.query_name_entry.pack(pady=(10, 0))

        self.query_class_label = tk.Label(teacher_window, text="班级：")
        self.query_class_label.pack()
        self.query_class_entry = tk.Entry(teacher_window)
        self.query_class_entry.pack(pady=(10, 0))

        self.query_button = tk.Button(teacher_window, text="查询", command=self.query_teacher)
        self.query_button.pack(pady=(10, 0))

        # 创建菜单
        self.menu_bar = tk.Menu(teacher_window)

        # 排名菜单
        self.rank_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.rank_menu.add_command(label="排名（升序）", command=lambda: self.show_rank(True))
        self.rank_menu.add_command(label="排名（降序）", command=lambda: self.show_rank(False))
        self.menu_bar.add_cascade(label="排名", menu=self.rank_menu)

        # 学号菜单
        self.student_id_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.student_id_menu.add_command(label="学号（升序）", command=lambda: self.show_student_id(True))
        self.student_id_menu.add_command(label="学号（降序）", command=lambda: self.show_student_id(False))
        self.menu_bar.add_cascade(label="学号", menu=self.student_id_menu)

        # 姓名菜单
        self.student_name_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.student_name_menu.add_command(label="姓名（升序）", command=lambda: self.show_student_name(True))
        self.student_name_menu.add_command(label="姓名（降序）", command=lambda: self.show_student_name(False))
        self.menu_bar.add_cascade(label="姓名", menu=self.student_name_menu)

        # 各科成绩菜单
        self.subject_grades_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.subject_grades_menu.add_command(label="数学成绩（升序）", command=lambda: self.show_subject_grades(True, "math"))
        self.subject_grades_menu.add_command(label="数学成绩（降序）", command=lambda: self.show_subject_grades(False, "math"))
        self.subject_grades_menu.add_command(label="英语成绩（升序）", command=lambda: self.show_subject_grades(True, "english"))
        self.subject_grades_menu.add_command(label="英语成绩（降序）", command=lambda: self.show_subject_grades(False, "english"))
        self.subject_grades_menu.add_command(label="科学成绩（升序）", command=lambda: self.show_subject_grades(True, "science"))
        self.subject_grades_menu.add_command(label="科学成绩（降序）", command=lambda: self.show_subject_grades(False, "science"))
        self.menu_bar.add_cascade(label="各科成绩", menu=self.subject_grades_menu)

        # 总成绩菜单
        self.total_grades_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.total_grades_menu.add_command(label="总成绩（升序）", command=lambda: self.show_total_grades(True))
        self.total_grades_menu.add_command(label="总成绩（降序）", command=lambda: self.show_total_grades(False))
        self.menu_bar.add_cascade(label="总成绩", menu=self.total_grades_menu)

        teacher_window.config(menu=self.menu_bar)

        # 初始化显示为空
        self.show_empty_result(teacher_window)

        # 增删改查操作按钮
        self.add_button = tk.Button(teacher_window, text="添加成绩", command=self.add_grade)
        self.add_button.pack(pady=(10, 0))
        self.delete_button = tk.Button(teacher_window, text="删除成绩", command=self.delete_grade)
        self.delete_button.pack()
        self.update_button = tk.Button(teacher_window, text="修改成绩", command=self.update_grade)
        self.update_button.pack(pady=(10, 0))

    def query_teacher(self):
        student_id = self.query_id_entry.get()
        student_name = self.query_name_entry.get()
        student_class = self.query_class_entry.get()

        # 构建查询语句
        query = "SELECT * FROM students WHERE 1=1"
        params = []
        if student_id:
            query += " AND student_id = %s"
            params.append(student_id)
        if student_name:
            query += " AND name = %s"
            params.append(student_name)
        if student_class:
            query += " AND class = %s"
            params.append(student_class)

        # 执行查询
        mycursor.execute(query, params)
        matching_students = mycursor.fetchall()

        if matching_students:
            self.show_query_results(matching_students)
        else:
            messagebox.showinfo("查询结果", "未找到匹配的学生信息。")

    def show_query_results(self, students_data):
        # 清空之前的显示
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.winfo_parent() == self.root:
                widget.destroy()

        for student in students_data:
            student_info = f"学号：{student[1]}, 姓名：{student[2]}, 班级：{student[3]}, 数学成绩：{student[4]}, 英语成绩：{student[5]}, 科学成绩：{student[6]}"
            tk.Label(self.root, text=student_info).pack()

    def show_empty_result(self, window):
        empty_label = tk.Label(window, text="暂无查询结果。")
        empty_label.pack()

    def show_rank(self, ascending=True):
        # 实现排名逻辑（这里只是简单示例，实际可能需要更复杂的计算和查询）
        query = "SELECT student_id, name, math_grade + english_grade + science_grade AS total_grade FROM students ORDER BY total_grade "
        if not ascending:
            query += "DESC"
        mycursor.execute(query)
        sorted_students = mycursor.fetchall()

        print(f"排名（{'升序' if ascending else '降序'}）:")
        for i, student in enumerate(sorted_students, start=1):
            print(f"{i}. 学号：{student[0]}, 姓名：{student[1]}, 总成绩：{student[2]}")

    def show_student_id(self, ascending=True):
        query = "SELECT * FROM students ORDER BY student_id "
        if not ascending:
            query += "DESC"
        mycursor.execute(query)
        sorted_students = mycursor.fetchall()

        print(f"学号（{'升序' if ascending else '降序'}）:")
        for student in sorted_students:
            print(f"学号：{student[1]}, 姓名：{student[2]}, 总成绩：{student[4] + student[5] + student[6]}")

    def show_student_name(self, ascending=True):
        query = "SELECT * FROM students ORDER BY name "
        if not ascending:
            query += "DESC"
        mycursor.execute(query)
        sorted_students = mycursor.fetchall()

        print(f"姓名（{'升序' if ascending else '降序'}）:")
        for student in sorted_students:
            print(f"学号：{student[1]}, 姓名：{student[2]}, 总成绩：{student[4] + student[5] + student[6]}")

    def show_subject_grades(self, ascending=True, subject="math"):  # 默认按数学成绩排序
        query = f"SELECT * FROM students ORDER BY {subject}_grade "
        if not ascending:
            query += "DESC"
        mycursor.execute(query)
        sorted_students = mycursor.fetchall()

        print(f"{subject}成绩（{'升序' if ascending else '降序'}）:")
        for student in sorted_students:
            print(f"学号：{student[1]}, 姓名：{student[2]}, {subject}成绩：{student[4] if subject =='math' else student[5] if subject == 'english' else student[6]}, 总成绩：{student[4] + student[5] + student[6]}")

    def show_total_grades(self, ascending=True):
        query = "SELECT student_id, name, math_grade + english_grade + science_grade AS total_grade FROM students ORDER BY total_grade "
        if not ascending:
            query += "DESC"
        mycursor.execute(query)
        sorted_students = mycursor.fetchall()

        self.show_query_results(sorted_students)

    def add_grade(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("添加成绩")

        # 设置窗口风格
        style = Style(theme="flatly")

        # 学号标签和输入框
        self.add_student_id_label = tk.Label(add_window, text="学号：")
        self.add_student_id_label.pack(pady=(30, 0))
        self.add_student_id_entry = tk.Entry(add_window)
        self.add_student_id_entry.pack()

        # 数学成绩标签和输入框
        self.math_grade_label = tk.Label(add_window, text="数学成绩：")
        self.math_grade_label.pack()
        self.math_grade_entry = tk.Entry(add_window)
        self.math_grade_entry.pack(pady=(10, 0))

        # 英语成绩标签和输入框
        self.english_grade_label = tk.Label(add_window, text="英语成绩：")
        self.english_grade_label.pack()
        self.english_grade_entry = tk.Entry(add_window)
        self.english_grade_entry.pack(pady=(10, 0))

        # 科学成绩标签和输入框
        self.science_grade_label = tk.Label(add_window, text="科学成绩：")
        self.science_grade_label.pack()
        self.science_grade_entry = tk.Entry(add_window)
        self.science_grade_entry.pack(pady=(10, 0))

        # 添加按钮
        self.add_
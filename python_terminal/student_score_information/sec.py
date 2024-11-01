import tkinter as tk
from tkinter import messagebox
import pymysql
# from ttkbootstrap import Style

# 连接到MySQL数据库
mydb = pymysql.Connection(
    host="localhost",
    user="root",
    password="123456",
    port=3306
)

mycursor = mydb.cursor()

# 检查数据库中是否存在必要的表，如果不存在则创建
def create_tables_if_not_exist():
    # 学生信息表
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        student_id VARCHAR(255) UNIQUE NOT NULL,
        gender VARCHAR(10),
        class VARCHAR(255) NOT NULL
    )
    """)

    # 成绩表
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id VARCHAR(255) NOT NULL,
       平时成绩 DECIMAL(5, 2),
        期中考试成绩 DECIMAL(5, 2),
        期末考试成绩 DECIMAL(5, 2),
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    )
    """)

# 全局变量用于存储当前登录用户信息和权限
current_user = None
current_user_role = None

class StudentGradeManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("学生成绩管理系统")

        # 设置窗口风格
        # style = Style(theme="flatly")

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

        # 注册按钮（如果需要注册功能）
        self.register_button = tk.Button(self.root, text="注册", command=self.register)
        self.register_button.pack()

        # 登录按钮
        self.login_button = tk.Button(self.root, text="登录", command=self.login)
        self.login_button.pack(pady=(10, 0))

        # 退出按钮
        self.exit_button = tk.Button(self.root, text="退出", command=self.root.quit)
        self.exit_button.pack()

    def register(self):
        # 注册窗口逻辑，这里可以添加对输入信息的验证等
        register_window = tk.Toplevel(self.root)
        register_window.title("注册")

        # 设置窗口风格
        # style = Style(theme="flatly")

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

        # 将新用户信息插入数据库（假设这里的注册用户都是学生，可根据实际需求扩展）
        mycursor.execute("INSERT INTO students (student_id, name, password) VALUES (%s, '默认姓名', %s)", (username, password))
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

        # 验证登录信息，这里可以根据不同的用户角色（如教师、学生、家长等）进行不同的查询和验证
        mycursor.execute("SELECT * FROM students WHERE student_id = %s AND password = %s", (username, password))
        result = mycursor.fetchone()
        if result:
            global current_user, current_user_role
            current_user = username
            current_user_role = "student"  # 这里简单假设登录成功的是学生角色，可根据实际情况扩展判断逻辑
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

        # 设置窗口属性
        teacher_window.geometry('500x500')
        teacher_window.resizable(False, False)
        teacher_window.iconbitmap('OIP-C_16X16.ico')
        teacher_window.configure(bg='white')
        teacher_window.attributes('-alpha', 1)

        # 成绩录入相关组件和按钮
        self.entry_student_id_label = tk.Label(teacher_window, text="学生学号：")
        self.entry_student_id_label.place(x=70, y=30)
        self.entry_student_id_entry = tk.Entry(teacher_window)
        self.entry_student_id_entry.place(x=140, y=30)

        self.ping_shi_cheng_ji_label = tk.Label(teacher_window, text="平时成绩：")
        self.ping_shi_cheng_ji_label.place(x=70, y=60)
        self.ping_shi_cheng_ji_entry = tk.Entry(teacher_window)
        self.ping_shi_cheng_ji_entry.place(x=140, y=60)

        self.qi_zhong_kao_shi_cheng_ji_label = tk.Label(teacher_window, text="期中考试成绩：")
        self.qi_zhong_kao_shi_cheng_ji_label.place(x=70, y=90)
        self.qi_zhong_kao_shi_cheng_ji_entry = tk.Entry(teacher_window)
        self.qi_zhong_kao_shi_cheng_ji_entry.place(x=140, y=90)

        self.qi_mo_kao_shi_cheng_ji_label = tk.Label(teacher_window, text="期末考试成绩：")
        self.qi_mo_kao_shi_cheng_ji_label.place(x=70, y=120)
        self.qi_mo_kao_shi_cheng_ji_entry = tk.Entry(teacher_window)
        self.qi_mo_kao_shi_cheng_ji_entry.place(x=140, y=120)

        self.enter_grade_button = tk.Button(teacher_window, text="录入成绩", command=self.enter_grades)
        self.enter_grade_button.place(x=100, y=150)

        # 查询按钮等其他组件（可以根据需要添加更多功能按钮和组件）
        self.query_button = tk.Button(teacher_window, text="查询成绩", command=self.query_teacher_grades)
        self.query_button.place(x=200, y=150)

        # 创建菜单等（可以进一步完善菜单功能，如添加系统设置等相关选项）
        self.menu_bar = tk.Menu(teacher_window)
        teacher_window.config(menu=self.menu_bar)

    def enter_grades(self):
        student_id = self.entry_student_id_entry.get()
        ping_shi_cheng_ji = self.ping_shi_cheng_ji_entry.get()
        qi_zhong_kao_shi_cheng_ji = self.qi_zhong_kao_shi_cheng_ji_entry.get()
        qi_mo_kao_shi_cheng_ji = self.qi_mo_kao_shi_cheng_ji_entry.get()

        try:
            # 将成绩转换为浮点数进行验证和插入
            ping_shi_cheng_ji = float(ping_shi_cheng_ji)
            qi_zhong_kao_shi_cheng_ji = float(qi_zhong_kao_shi_cheng_ji)
            qi_mo_kao_shi_cheng_ji = float(qi_mo_kao_shi_cheng_ji)

            # 检查学号是否存在于学生表中
            mycursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            if not mycursor.fetchone():
                messagebox.showerror("录入失败", "该学号不存在，请先确认学生信息。")
                return

            # 插入成绩到成绩表中
            mycursor.execute("INSERT INTO grades (student_id, 平时成绩, 期中考试成绩, 期末考试成绩) VALUES (%s, %s, %s, %s)",
                             (student_id, ping_shi_cheng_ji, qi_zhong_kao_shi_cheng_ji, qi_mo_kao_shi_cheng_ji))
            mydb.commit()
            messagebox.showinfo("录入成功", "成绩录入成功！")
        except ValueError:
            messagebox.showerror("录入失败", "成绩必须为数字。")

    def query_teacher_grades(self):
        # 查询成绩的逻辑，可以根据教师的需求进行定制，比如查询某个班级的所有学生成绩等
        pass

    def show_student_interface(self):
        student_window = tk.Toplevel(self.root)
        student_window.title("学生界面")

        # 设置窗口属性
        student_window.geometry('400x300')
        student_window.resizable(False, False)
        student_window.configure(bg='white')

        # 查询成绩按钮等组件
        self.query_own_grades_button = tk.Button(student_window, text="查询我的成绩", command=self.query_student_grades)
        self.query_own_grades_button.pack(pady=(50, 0))

    def query_student_grades(self):
        # 根据当前登录学生的学号查询成绩
        mycursor.execute("SELECT g.* FROM grades g JOIN students s ON g.student_id = s.student_id WHERE s.student_id = %s", (current_user,))
        result = mycursor.fetchone()
        if result:
            messagebox.showinfo("成绩查询结果", f"平时成绩：{result[2]}, 期中考试成绩：{result[3]}, 期末考试成绩：{result[4]}")
        else:
            messagebox.showinfo("成绩查询结果", "暂无成绩记录。")

    def show_parent_interface(self):
        parent_window = tk.Toplevel(self.root)
        parent_window.title("家长界面")

        # 设置窗口属性
        parent_window.geometry('400x300')
        parent_window.resizable(False, False)
        parent_window.configure(bg='white')

        # 查询输入框和标签（假设家长只能查询与当前登录学生相关信息，这里学号固定为当前登录学生学号）
        self.query_id_label = tk.Label(parent_window, text="学号：")
        self.query_id_label.pack(pady=(30, 0))
        self.query_id_entry = tk.Entry(parent_window)
        self.query_id_entry.pack()
        self.query_id_entry.insert(0, current_user)  # 自动填入当前学生学号
        self.query_id_entry.config(state='readonly')  # 设置为只读

        self.query_button = tk.Button(parent_window, text="查询", command=self.query_parent_grades)
        self.query_button.pack(pady=(10, 0))

    def query_parent_grades(self):
        # 查询当前学生的成绩并显示给家长
        mycursor.execute("SELECT g.* FROM grades g JOIN students s ON g.student_id = s.student_id WHERE s.student_id = %s", (current_user,))
        result = mycursor.fetchone()
        if result:
            messagebox.showinfo("成绩查询结果", f"平时成绩：{result[2]}, 期中考试成绩：{result[3]}, 期末考试成绩：{result[4]}")
        else:
            messagebox.showinfo("成绩查询结果", "暂无成绩记录。")

# 成绩统计分析功能（示例函数，可根据实际需求扩展）
def generate_report():
    # 这里可以实现更复杂的成绩统计分析逻辑，比如计算平均分、排名等，并生成报告
    mycursor.execute("SELECT AVG(平时成绩), AVG(期中考试成绩), AVG(期末考试成绩) FROM grades")
    averages = mycursor.fetchone()
    messagebox.showinfo("学业表现报告", f"平均平时成绩：{averages[0]}, 平均期中考试成绩：{averages[1]}, 平均期末考试成绩：{averages[2]}")

# 主程序入口
if __name__ == "__main__":
    create_tables_if_not_exist()
    app = StudentGradeManagementSystem()
    app.root.mainloop()
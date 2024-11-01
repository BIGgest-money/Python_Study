
from tkinter import *
import pymysql
# 创建连接数据库student的对象conn
conn = pymysql.connect(
    host='localhost',  # 数据库主机名
    port=3306,  # 数据库端口号，默认为3306
    user='root',  # 数据库用户名
    password='123456',  # 数据库密
    autocommit=True  # 设置修改数据无需确认
)
sort_student = int(0)
sort_data = int(0)

# 获取游标对象
cursor = conn.cursor()

# 创建数据库，若有则不创建
cursor.execute("create database if not exists information")
conn.select_db("information") # 建立与数据库的连接

# 创建学生信息表， 若有则不创建
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    id int,
    name varchar(10),
    kulas varchar(10),
    math int,
    english int,
    computer int,
    total int
);""")

#
#
# # 创建成绩表（Courses）的SQL语句
# cursor.execute( """
#     CREATE TABLE if not exists Courses (
#     CourseID VARCHAR(255) NOT NULL PRIMARY KEY,
#     CourseName VARCHAR(255) NOT NULL,
#     CourseDescription TEXT
# );""")
#
# # 创建成绩表（Scores）的SQL语句
# cursor.execute("""
#     CREATE TABLE if not exists Scores (
#     ScoreID VARCHAR(255) NOT NULL PRIMARY KEY,
#     StudentID VARCHAR(255),
#     CourseID VARCHAR(255),
#     RegularGrade DECIMAL(5, 2),
#     MidtermGrade DECIMAL(5, 2),
#     FinalGrade DECIMAL(5, 2),
#     FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
#     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
# );""")
#
# # 创建学生成绩查询表（ScoreQueries）的SQL语句
# cursor.execute ( """
#     CREATE TABLE if not exists ScoreQueries (
#     QueryID VARCHAR(255) NOT NULL PRIMARY KEY,
#     UserType VARCHAR(255),
#     StudentID VARCHAR(255),
#     NamePattern VARCHAR(255),
#     ClassPattern VARCHAR(255),
#     CourseNamePattern VARCHAR(255),
#     FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
# );""")
#
# # 创建数据统计与分析表（Statistics）的SQL语句
# cursor.execute( """
#     CREATE TABLE if not exists Statistics (
#     StatID VARCHAR(255) NOT NULL PRIMARY KEY,
#     StatType VARCHAR(255),
#     QueryID VARCHAR(255),
#     Result VARCHAR(255),
#     FOREIGN KEY (QueryID) REFERENCES ScoreQueries(QueryID)
# );""")
#
# # 创建异常数据处理与提醒功能表（ExceptionDataHandling）的SQL语句
# cursor.execute( """
#     CREATE TABLE if not exists ExceptionDataHandling (
#     Id VARCHAR(255) NOT NULL PRIMARY KEY,
#     DataType VARCHAR(255),
#     ExceptionRule TEXT,
#     LastRunTime TIMESTAMP,
#     LogEntries TEXT,
#     Notifications TEXT
# );""")
#
#
#
# # 创建数据导出与导入功能表（DataExportImport）的SQL语句
# cursor.execute("""
#     CREATE TABLE if not existsDataExportImport (
#     Id VARCHAR(255) NOT NULL PRIMARY KEY,
#     DataType VARCHAR(255),
#     ExportFormat VARCHAR(255),
#     QueryConditions TEXT,
#     ExportResult TEXT,
#     ImportResult TEXT
# );""")
# # 创建学生信息维护功能表（StudentInformationManagement）的SQL语句
# cursor.execute( """
#     CREATE TABLE if not exists StudentInformationManagement (
#     StudentId VARCHAR(255),
#     StudentName VARCHAR(255),
#     Gender VARCHAR(10),
#     Class VARCHAR(255),
#     OperationType VARCHAR(255),
#     OperationStatus VARCHAR(255),
#     OperationTimestamp TIMESTAMP,
#     NotificationMessage TEXT
# );""")
#
# # 创建学生成绩录入与修改功能表（StudentGrades）的SQL语句
# cursor.execute("""
#     CREATE TABLE if not exists StudentGrades (
#     StudentId VARCHAR(255),
#     SubjectName VARCHAR(255),
#     GradeType VARCHAR(255),
#     GradeValue DECIMAL(5, 2),
#     OperationType VARCHAR(255),
#     OperationTimestamp TIMESTAMP,
#     NotificationMessage TEXT
# );""")
#
# # 创建学生信息提醒功能表（StudentInformationAudit）的SQL语句
# cursor.execute("""
#     CREATE TABLE if not exists StudentInformationAudit (
#     StudentId VARCHAR(255),
#     StudentName VARCHAR(255),
#     Class VARCHAR(255),
#     AuditStatus VARCHAR(255),
#     AuditTimestamp TIMESTAMP,
#     AuditUser VARCHAR(255),
#     AuditComment TEXT
# );""")
#
# # 创建学生信息归档功能表（StudentInformationArchive）的SQL语句
# cursor.execute("""
#     CREATE TABLE if not exists StudentInformationArchive (
#     StudentId VARCHAR(255),
#     StudentName VARCHAR(255),
#     Class VARCHAR(255),
#     ArchiveConditions VARCHAR(255),
#     ArchiveMethod VARCHAR(255),
#     ArchiveTimestamp TIMESTAMP,
#     ArchiveFilePath VARCHAR(255)
# );""")
#
#
#
# # 创建班级信息表（ClassInformation）的SQL语句
# cursor.execute("""
#     CREATE TABLE if not exists ClassInformation (
#     ClassID VARCHAR(255) NOT NULL PRIMARY KEY,
#     ClassName VARCHAR(255),
#     Grade VARCHAR(255),
#     ClassAdviser VARCHAR(255),
#     CreatedAt TIMESTAMP,
#     UpdatedAt TIMESTAMP
# );""")
#
# # 创建教师信息表（TeacherInformation）的SQL语句
# cursor.execute("""
#     CREATE TABLE if not exists TeacherInformation (
#     TeacherID VARCHAR(255) NOT NULL PRIMARY KEY,
#     TeacherName VARCHAR(255),
#     SubjectName VARCHAR(255),
#     CreatedAt TIMESTAMP,
#     UpdatedAt TIMESTAMP
# );""")
#

# 创建账号密码表，若有则不创建
cursor.execute("""CREATE TABLE IF NOT EXISTS admin_name_pwd(
    name varchar(10),
    pwd varchar(10)
);""")



# 判断登录的账号密码是否都正确
def check_login(uname, pwd):
    cursor.execute("select * from admin_name_pwd")
    results = cursor.fetchall()
    # print(results)
    for na, pd in results:
        if na == uname and pd == pwd:
            return True, '登录成功'
    return False, '登录失败,账号或密码错误'

# 添加正确注册的账号以及密码
def add_admin_name_pwd(uname, pwd):
    cursor.execute("insert into admin_name_pwd values('{0}', '{1}');".format(uname, pwd))
# add_admin_name_pwd("123", "123")

# 检验注册的账号名称是否已经存在
def check_usname(uname):
    cursor.execute("select count(*) from admin_name_pwd anp where name = '{0}';".format(uname))
    res = cursor.fetchall()
    if res[0][0]:
        return True
    return False


# 获取数据库中学生所有信息，按给定的信息给出
# 通过全局变量sort_data以及sort_student
# sort_student 为0代表升序，为一代表降序
def all():
    if sort_student == 1:
        if sort_data == 0:
            cursor.execute("select * from students order by id;")
        elif sort_data == 1:
            cursor.execute("select * from students order by total;")
        elif sort_data == 2:
            cursor.execute("select * from students order by math;")
        elif sort_data == 3:
            cursor.execute("select * from students order by english;")
        elif sort_data == 4:
            cursor.execute("select * from students order by computer;")
    else:
        if sort_data == 0:
            cursor.execute("select * from students order by id desc;")
        elif sort_data == 1:
            cursor.execute("select * from students order by total desc;")
        elif sort_data == 2:
            cursor.execute("select * from students order by math desc;")
        elif sort_data == 3:
            cursor.execute("select * from students order by english desc;")
        elif sort_data == 4:
            cursor.execute("select * from students order by computer desc;")
    data = cursor.fetchall()
    key = ('id', 'name', 'kulas', 'math', 'english', 'computer', 'total')
    jsonList = []
    # 通过数据得到的数据是元组类型，需要压缩成字典类型便于输出
    for i in data:
        jsonList.append(dict(zip(key, i)))
    return jsonList

# 查询录入的学号是否存在

def check_student_id(id):
    cursor.execute("select count(*) from students where id = '{0}';".format(id))
    res = cursor.fetchall()
    if res[0][0]:
        return False, "该学号已存在请重新输入"
    return True, '录入成功'


# 单独查询某个班级的成绩
def search_kulas(kulas_value):
    cursor.execute("select * from students where kulas = '{0}';".format(kulas_value))
    data = cursor.fetchall()
    key = ('id', 'name', 'kulas', 'math', 'english', 'computer', 'total')
    jsonList = []
    # 通过数据得到的数据是元组类型，需要压缩成字典类型便于输出
    for i in data:
        jsonList.append(dict(zip(key, i)))
    return jsonList
# 插入一条学生信息
def insert(stu):
    cursor.execute("insert into students values('{0}', '{1}', '{2}','{3}', '{4}', '{5}', '{6}');".
                   format(stu[0], stu[1], stu[2], stu[3], stu[4], stu[5], stu[6]))

# 通过id来删除学生信息
def delete_id(user_id):
    cursor.execute("select count(*) from students where id = '{0}';".format(user_id))
    res = cursor.fetchall()
    if res[0][0]:
        cursor.execute("delete from students where id = '{0}';".format(user_id))
        return True, '删除成功'
    else: return False, '学号为' + str(user_id) + '的学生不存在'

# 通过名字来删除学生信息
def delete_name(user_name):
    cursor.execute("select count(*) from students where name = '{0}';".format(user_name))
    res = cursor.fetchall()
    # print(res)
    if res[0][0]:
        cursor.execute("delete from students where name = '{0}';".format(user_name))
        return True, '删除成功'
    else: return False, '姓名为' + str(user_name) + '的学生不存在'


# 通过id来查询学生的信息
def search_id(user_id):
    cursor.execute("select count(*) from students where id = '{0}';".format(user_id))
    res = cursor.fetchall()
    if res[0][0]:
        cursor.execute("select * from students where id = '{0}';".format(user_id))
        stu = cursor.fetchall()
        return True, stu
    else:
        return False, '学号为' + str(user_id) + '的学生不存在'

# 通过学生姓名来查询剩余的信息
def search_name(user_name):
    cursor.execute("select count(*) from students where name = '{0}';".format(user_name))
    res = cursor.fetchall()
    if res[0][0]:
        cursor.execute("select * from students where name = '{0}';".format(user_name))
        stu = cursor.fetchall()
        return True, stu
    else:
        return False, '名字为' + str(user_name) + '的学生不存在'


tuple = (
         (1, '李胜利', '软件开发4班', 68, 59, 86, 213),
         (2, '荣浩', '软件开发4班', 56, 83, 20, 159),
         (3, '刘泽', '软件开发4班', 78, 83, 89, 250),
         (4, '陈梁', '软件开发4班', 68, 99, 67, 234),
         (5, '宋明玉', '软件开发4班', 79, 72, 90, 241),
         (6, '邓海洋', '软件开发4班', 68, 47, 89, 204),
         (7, '快乐男孩', '软件开发4班', 79, 78, 48, 205),
         (8, '周解青', '软件开发4班', 69, 78, 82, 229),
         (9, '帅哥', '软件开发4班', 72, 47, 88, 207),
         (10, '金十一', '物联网3班', 84, 68, 92, 244),
         (11, '郑十', '物联网2班', 81, 75, 88, 244),
         (12, '吴九', '大数据1班', 92, 87, 61, 240),
         (13, '周八', '软件土木3班', 87, 71, 92, 250),
         (14, '孙七', '计算机1班', 64, 76, 83, 223),
         (15, '赵六', '软件开发4班', 48, 86, 75, 209),
         (16, '王五', '软件金融2班', 78, 92, 62, 232),
         (17, '李四', '软件会计2班', 80, 83, 45, 208),
         (18, '张三', '软件土木5班', 61, 72, 77, 210),
         (19, '陈二', '计算机5班', 81, 67, 72, 220),
         (20, '刘一', '软件开发4班', 60, 85, 67, 212))

# 手动解除即可将这些信息添加进数据库中，使用之后需重新注释

# 往student中加入信息，若有则不加入
for stu in tuple:
    if check_student_id(stu[0])[0] == True:
        insert(stu)

# 加入初始账号，若有则不加入
if check_usname("root") == False:
    add_admin_name_pwd('root', 'root')
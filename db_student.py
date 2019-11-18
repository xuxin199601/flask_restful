import MySQLdb

host = "localhost"
port = 3306
user = "root"
passwd = ""
db = "students"
conn = None
cur = None

# 执行数据库操作之前判断数据库连接是否OK，如果异常则创建一次连接
def db_opt(func):
    def db_ping():
        global conn, cur
        try:
            cur.execute("select 1")
            cur.fetchone()
        except:
            # conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset="utf8")
            conn = MySQLdb.connect("localhost", "root", "", "students", charset='utf8')
            cur = conn.cursor()
            print("build a new connection")

    def wrapper(*args, **kwargs):
        global conn, cur

        try:
            db_ping()
            res =  func(*args, **kwargs)
            print("db_opt", func, args, res)
            return res
        except:
            return {'status':False, 'data':'db operation maybe have some errors.'}
    return wrapper

class DbStudent:
    # 根据student_id获取学生信息
    @staticmethod
    @db_opt
    def get_student_by_id(student_id):
        sql = 'select id, name, age from student where id = %s' % student_id
        cur.execute(sql)
        res = cur.fetchall()
        if len(res) == 0:
            return {}
        else:
            (id, name, age) = res[0]
            dict_student ={}
            dict_student['id'] = id
            dict_student['name'] = name
            dict_student['age'] = age
            return dict_student

    # 根据name获取学生信息
    @staticmethod
    @db_opt
    def get_student_by_name(name):
        sql = 'select id, name, age from student where name = "%s"' % name
        cur.execute(sql)
        res = cur.fetchall()
        if len(res) == 0:
            return {}
        else:
            (id, name, age) = res[0]
            dict_student = {}
            dict_student['id'] = id
            dict_student['name'] = name
            dict_student['age'] = age
            return dict_student

    # 根据student_id更新学生信息
    @staticmethod
    @db_opt
    def update_student_by_id(student_id, student_info):
        sql = 'update student set name = "%s", age = %s where id = %s' % \
              (student_info['name'], student_info['age'], student_id)
        print(sql)
        cur.execute(sql)
        conn.commit()
        return DbStudent.get_student_list()

    # 增加一条学生信息
    @staticmethod
    @db_opt
    def insert_student(student_info):
        sql = 'insert into student(id, name, age) values(%s, "%s", %s)' % \
              (student_info['id'], student_info['name'], student_info['age'])
        print(sql)
        cur.execute(sql)
        conn.commit()
        return DbStudent.get_student_list()

    # 根据student_id删除学生信息（更新is_del字段）
    @staticmethod
    @db_opt
    def delete_student_by_id(student_id):
        sql = "delete from student where id = %s" % student_id
        print(sql)
        cur.execute(sql)
        conn.commit()
        return DbStudent.get_student_list()

    # 获取学生信息列表
    @staticmethod
    @db_opt
    def get_student_list():
        sql = 'select id, name, age from student'
        cur.execute(sql)
        res = cur.fetchall()
        if len(res) == 0:
            return {}
        else:
            student_list = []
            for (id, name, age) in res:
                dict_student = {}
                dict_student['id'] = id
                dict_student['name'] = name
                dict_student['age'] = age
                student_list.append( dict_student )
            return {"student_list": student_list}

if __name__ == '__main__':
    print(DbStudent.get_student_by_id(1))
    print(DbStudent.get_student_by_name('小明'))
    print(DbStudent.get_student_list())
    print(DbStudent.delete_student_by_id(2))

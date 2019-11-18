from flask_restful import reqparse, abort, Api, Resource
from db_student import DbStudent

# 404操作
def abort_if_todo_doesnt_exist(student_id):
    if DbStudent.get_student_by_id(student_id) == {}:
        abort(404, message="Todo {} doesn't exist".format(student_id))

# 入参解析器
parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('age')

# 学生信息操作
class Student(Resource):
    def __init__(self):
        pass

    # 获取student信息
    def get(self, student_id):
        abort_if_todo_doesnt_exist(student_id)
        res = DbStudent.get_student_by_id(student_id)
        return res, 200

    # 更新student信息
    def put(self, student_id):
        print("put come in")
        abort_if_todo_doesnt_exist(student_id)
        args = parser.parse_args()
        print(args)
        res = DbStudent.update_student_by_id(student_id, args)
        return res, 200

    # 删除student信息
    def delete(self, student_id):
        print("put come in")
        abort_if_todo_doesnt_exist(student_id)
        res = DbStudent.delete_student_by_id(student_id)
        return res, 200

    # 兼容post操作，获取student信息
    def post(self, student_id):
        print("post come in")
        return self.get(student_id)

# 学生列表操作
class StudentList(Resource):
    # 获取学生信息列表
    def get(self):
        res = DbStudent.get_student_list()
        return res, 200

    # 增加单个学生信息
    def post(self):
        args = parser.parse_args()
        res = DbStudent.insert_student(args)
        return res, 200

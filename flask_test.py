# coding:utf8
from flask import Flask, render_template, request
from flask_restful import Api

from ctrl_student import StudentList, Student

app = Flask(__name__)
api = Api(app)
api.add_resource(StudentList, '/student/')
api.add_resource(Student, '/student/<student_id>')

@app.before_request
def before_request():
    ip = request.remote_addr
    url = request.url
    form = request.form # 请求的数据，可执行searchword = request.form.get('key', '')  ?????????测试（带参数的post请求）过程中form为空，不清楚原因
    args = request.args # ?key=value，可执行searchword = request.args.get('key', '')
    values = request.values # form和args的元组
    headers = request.headers
    method = request.method
    path = request.path
    base_url = request.base_url
    url_root = request.url_root
    print("ip", ip)
    print("url", url)
    # print "form", form
    # print "args", args
    # print "values", values
    # print "headers", headers
    # print "method", method
    # print "path", path
    # print "base_url", base_url
    # print "url_root", url_root

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

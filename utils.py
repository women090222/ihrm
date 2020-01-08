import app
import json
import pymysql


# 编写断言代码函数
def assert_common(self, response, http_code, success, code, message):
    # 断言响应状态码
    # response.json().get(),字典的查询方法
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get('success'))  # 断言success的值
    self.assertEqual(code, response.json().get('code'))  # 断言code的值
    self.assertIn(message, response.json().get('message'))  # 断言message的值


def read_login_data():
    data_path = app.BASE_DIR + '/data/login_data.json'
    with open(data_path, mode='r', encoding='utf-8') as f:
        # 加载文件为json格式的数据
        jsonData = json.load(f)
        # 遍历文件取出其中数据并保存到列表中
        p_list = []
        for data in jsonData:
            mobile = data.get('mobile')
            password = data.get('password')
            http_code = data.get('http_code')
            success = data.get('success')
            code = data.get('code')
            message = data.get('message')
            p_list.append((mobile, password, http_code, success, code, message))
        print(p_list)
        return p_list


def read_add_emp_data():
    path = app.BASE_DIR + '/data/emp_data.json'
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        # 由于emp_data.json是字段数据，可以使用字典的get方法获取其中参数
        add_emp_data = jsonData.get('add_emp')
        result_list = []
        username = add_emp_data.get('username')
        mobile = add_emp_data.get('mobile')
        success = add_emp_data.get('success')
        code = add_emp_data.get('code')
        message = add_emp_data.get('message')
        http_code = add_emp_data.get('http_code')
        result_list.append((username, mobile, success, code, message, http_code))

    print('读取添加员工的数据:', result_list)
    return result_list


def read_query_emp_data():
    path = app.BASE_DIR + '/data/emp_data.json'
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json文件
        jsonData = json.load(f)
        # 由于emp_data.json是字段数据，可以使用字典的get方法获取其中参数
        result_list = []
        query_emp_data = jsonData.get('query_emp')
        success = query_emp_data.get('success')
        code = query_emp_data.get('code')
        message = query_emp_data.get('message')
        http_code = query_emp_data.get('http_code')
        result_list.append((success, code, message, http_code))

    print('查询员工的数据:', result_list)
    return result_list


def read_modify_emp_data():
    path = app.BASE_DIR + '/data/emp_data.json'
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json文件
        jsonData = json.load(f)
        # 由于emp_data.json是字段数据，可以使用字典的get方法获取其中参数
        result_list = []
        modify_emp_data = jsonData.get('query_emp')
        username = modify_emp_data.get('username')
        success = modify_emp_data.get('success')
        code = modify_emp_data.get('code')
        message = modify_emp_data.get('message')
        http_code = modify_emp_data.get('http_code')
        result_list.append((username, success, code, message, http_code))
    print('修改员工的数据:', result_list)
    return result_list


def read_delete_emp_data():
    path = app.BASE_DIR + '/data/emp_data.json'
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json文件
        jsonData = json.load(f)
        # 由于emp_data.json是字段数据，可以使用字典的get方法获取其中参数
        result_list = []
        delete_emp_data = jsonData.get('query_emp')
        success = delete_emp_data.get('success')
        code = delete_emp_data.get('code')
        message = delete_emp_data.get('message')
        http_code = delete_emp_data.get('http_code')
        result_list.append((success, code, message, http_code))
    print('删除员工的数据:', result_list)
    return result_list


class DBUtils:

    def __init__(self, host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # __enter__和__exit__是一对魔法方法，主要是和with结合使用
    # 如：with DBUtils as db：
    # 我们就可以在with的代码中使用db来执行sql语句，这个db就相当于cursor
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    # 自定义建立连接数据库的函数
    def connect(self, host, user, password, database):
        conn = pymysql.connect(host, user, password, database)
        return conn


if __name__ == '__main__':
    # main函数的作用？
    # 防止调用这个模块或者类时,自动执行代码
    read_modify_emp_data()

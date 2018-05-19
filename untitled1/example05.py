import pymysql

from hrs import Dept


def main():
    config = {
        'host': 'localhost',
        'user': 'root',
        'passwd': '123456',
        'db': 'hrs',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor
    }
    conn = pymysql.connect(**config)
    try:
        uid = input('用户名: ')
        pwd = input('密码: ')
        with conn.cursor() as cursor:
            # 注射攻击的万能密码: a' or '1'='1
            """
            sql = "select 'x' from tb_user where username='%s' \
                     and userpass='%s'" % (uid, pwd)
            if cursor.execute(sql) > 0:
            """
            # cursor.callproc('sp_dept_avg_sal', ())
            # 定义存储过程 / PyMySQL调用存储过程
            if cursor.execute(
                    'select 1 from tb_user where username=%s and userpass=%s',
                    (uid, pwd)):
                print('登录成功, 开始使用系统')
            else:
                print('用户名或密码错误')
    finally:
        conn.close()


if __name__ == '__main__':
    main()

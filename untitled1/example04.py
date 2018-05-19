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
        with conn.cursor() as cursor:
            cursor.execute(
                'select dno no, dname name, dloc loc from tbdept')
            result = cursor.fetchone()
            while result:
                # 关系型数据库 - 关系模型
                # Python程序 - 对象模型
                # ORM - Object Relation Mapping - Alchemy
                # 有了ORM以后操作数据库就再也不用写SQL
                dept = Dept(**result)
                print(dept.no, dept.name, dept.location)
                result = cursor.fetchone()
    finally:
        conn.close()


if __name__ == '__main__':
    main()

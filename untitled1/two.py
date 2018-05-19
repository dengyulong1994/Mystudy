import pymysql

from hrs import Dept


def main():
    # 创建connection对象 连接数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='123456',
                           db='hrs', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        # 创建Cursor对象，发送命令
        with conn.cursor() as cursor:


            cursor.execute('select dno, dname, dloc from tbdept')
            result = cursor.fetchone()
            print(result)

            while result:
                # 关系型数据库 -- 关系模型
                # python程序  -- 对象模型
                # ORM -- Object Relation Mapping
                # Alchemy
                # 有了ORM以后操作数据库就不再用写SQL
                dept = Dept(**result)
                print(dept.dname)
                result = cursor.fetchone()

    finally:
        conn.close()

if __name__ == '__main__':
    main()
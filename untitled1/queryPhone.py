import pymysql

from hrs import Phone


def main():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='myphone', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            who = input('请输入你要查询的名字：')
            cursor.execute('select pname, pnum, qq, email from tb_phone2 where pname=%s',(who, ))
            result = cursor.fetchone()
            print(result)
            while result:
                phone = Phone(**result)
                print(phone.pname)
                print(phone.pnum)
                print(phone.qq)
                print(phone.email)
                result = cursor.fetchone()

    finally:
        conn.close()

if __name__ == '__main__':
    main()
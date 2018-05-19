import pymysql

def main():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456',
                           db='myphone', charset='utf8')
    try:
        with conn.cursor() as cursor:
            pname = input('输入名字：')
            pnum = input('输入电话：')
            qq = input('输入QQ：')
            email = input('输入邮箱：')

            cursor.execute('insert into tb_phone2 values (%s, %s, %s, %s)', (pname, pnum, qq, email))
            conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()









if __name__ == '__main__':
    main()
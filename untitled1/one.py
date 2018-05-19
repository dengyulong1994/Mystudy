import pymysql
# 事务的特点是什么？  -- ACID特性
# 原子性（Atomicity）：不可分割要么全成功要么全失败
# 一致性（Consistency）：事务前后数据状态要保持一致
# 隔离性（Isolation）：多个事务不能看到彼此的中间状态（提交或者回滚之前的状态）
# 持久性（Duration）：事务完成后数据要持久化（事务影响要反映在物理存储上）
def main():
    # 创建connection对象 连接数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='123456',
                           db='hrs', charset='utf8')
    try:
        # 创建Cursor对象，发送命令
        with conn.cursor() as cursor:
            # 向数据库发送QSL语句
            # execute 方法返回受影响的行数
            dno = input('部门编号：')
            # dname = input('部门名称：')
            # dloc = input('部门所在地：')
            # result = cursor.execute('insert into tbdept values (%s, %s, %s)', (dno, dname, dloc))
            result = cursor.execute('delete from tbdept where dno=%s', (dno, ))
            print('删除成功' if result == 1 else '删除失败')
            # 手动提交之前的操作
            conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    main()
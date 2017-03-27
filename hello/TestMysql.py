# coding:utf-8
import MySQLdb


def insert():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="2008", db="yahier");
    cursor = conn.cursor();
    sql = "insert into user(name)values('soso')";
    n = cursor.execute(sql);
    conn.commit();


def getDBConnect():
    return MySQLdb.connect(host="localhost", user="root", passwd="008", db="yahier")


def getDBCursor():
    conn = getDBConnect()
    return conn.cursor();



def updateIndex(index):
    sql = "update user set name = 'holy' where id = 10000"
    conn = getDBConnect();
    cursor = conn.cursor();
    line = cursor.execute(sql);
    print("影响的行数:" + str(line))
    conn.commit();


# 调用失败 db名称错误，但我也不记得db名称了
def show_question_data():
    sql = "select * from Question"
    conn = MySQLdb.connect(host="localhost", user="root", passwd="008", db="ModelS")
    cursor = conn.cursor()
    line = cursor.execute(sql)
    print("影响的行数:" + str(line))
    conn.commit();

# 调用ok
def show_user_data():
    sql = "select * from user"
    conn = MySQLdb.connect(host="localhost", user="root", passwd="008", db="yahier")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # 因为是tuple,所以可以这样使用结果集
    print result   # 打印过的结果为((10000L, 'bingo'), (10001L, 'bingo'))



show_question_data()
# updateIndex(1);
# show_user_data()
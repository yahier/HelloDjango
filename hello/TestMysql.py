# coding:utf-8
import MySQLdb


def insert():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="2008", db="yahier");
    cursor = conn.cursor();
    sql = "insert into user(name)values('soso')";
    n = cursor.execute(sql);
    conn.commit();


def getDBConnect():
    return MySQLdb.connect(host="localhost", user="root", passwd="2008", db="yahier");


def getDBCursor():
    conn = getDBConnect()
    return conn.cursor();


def updateIndex(index):
    sql = "update user set name = 'bingo' where id = 2"
    conn = getDBConnect();
    cursor = conn.cursor();
    line = cursor.execute(sql);
    print("影响的行数" + str(line))
    conn.commit();


updateIndex(1);

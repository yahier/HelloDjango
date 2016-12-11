# coding:utf-8
import sqlite3

#怎么访问settingS文件中的BASE_URL属性呢
def getSettingPyAttribute():
    print()


def insert():
    con = sqlite3.connect("python_sqlite_test.db")
    cursor = con.cursor()
    cursor.execute("create table if not exists user(name text,age int)")
    cursor.execute("insert into user values('soso',23)")
    con.commit()
    con.close()


def select():
    con = sqlite3.connect("python_sqlite_test.db")
    cursor = con.cursor()
    cursor.execute('SELECT * FROM user')
    print(cursor.fetchall())



select()







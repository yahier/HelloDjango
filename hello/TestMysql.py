import MySQLdb

def insert():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="2008", db="yahier");
    cursor = conn.cursor();
    sql = "insert into user(name)values('soso')";
    n = cursor.execute(sql);
    conn.commit();


insert()

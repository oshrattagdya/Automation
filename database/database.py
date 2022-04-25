import mysql.connector

# class Connector:
#     def __init__(self):
#         pass
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="10203040",
#         database="sakila"
#     )
        # print(mydb.cursor)
        # mycursur=mydb.cursor()
        # cur = mydb.cursor()
        #
        # sql = "show tables"
        # cur.execute(sql)
        # for t in cur:
        #     print(t)


#יש להגדיר CLASS של התחברות לבסיס נתונים ת בתווכו תהיה מתודה של התחברות
#יש לשלוף את כל השחקנים מטבלת שחקנים
#בנוסף את כל הסרטים
#ולהדפיס כל אחת מהתוצאות
#יש למנות את כמות הסרטים וכמות השחקנים

class DB :
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="10203040",
            database="sakila"
    )

    def connect(self,sql,type):
        connect = self.con.cursor()
        connect.execute(sql)
        if type == "select":
            return connect.fetchall()
        else:
            self.con.commit()
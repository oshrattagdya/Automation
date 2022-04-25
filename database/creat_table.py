#ייבוא ספרייה שבאמצעותה נתחבר ל DATABASEוהכנסת פרטי התחברות
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="10203040",
    database="sakila"
    )


mycursor = mydb.cursor()

#יצירת טבלה חדשה עם 2 ערכים שייהיו בטבלה
#
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)
# mycursor.execute("SHOW TABLES")

#הזנת כמה ערכים בו זמנית
#לששים לב שהEXECUTE זזה השתנה ל-executemany

# sql = "INSERT INTO students (name, address) VALUES (%s, %s)"
# val =[
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
#     ]
# mycursor.executemany(sql,val)
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

#קריאה לנתונים ספציפים מתוך הטבלה והצגת הנתונים היא לפי הסדר א-ב

mycursor.execute("SELECT name, address FROM students order by name ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#קריאה לנתון שמתחיל רק באות A
# sql = "SELECT * FROM students WHERE address regexp '^[a]'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


#מחיקת נתון מהטבלה שמתחיל באות A

sql = "DELETE FROM students WHERE address regexp '^[a]'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


#עדכון נתונים בטבלה

sql = "UPDATE students SET address = 'Canyon 123' WHERE address = 'mishol shimshon 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
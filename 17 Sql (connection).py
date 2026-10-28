import mysql.connector
print("hello world")
mycon=mysql.connector.connect(host='127.0.0.1',port='3306',database='flipkart',
                              user='root',password='VIGNESH@sql18')
mycursor=mycon.cursor()
sql="select * from products"
mycursor.execute(sql)
mydata=mycursor.fetchall()
for x in mydata:
    print(x)
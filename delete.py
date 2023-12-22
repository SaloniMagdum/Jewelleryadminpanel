#!C:\Python310-32\python.exe
import cgi
import mysql.connector
print("Content-Type: text/html\n")
import cgi,cgitb
cgitb.enable()

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suraj"
)
if conn.is_connected():
    dbcursor=conn.cursor()
    id=input("Enter id")
    query = "delete from addnew where id="+str(id)
    dbcursor.execute(query)
    conn.commit()
    print('<script>alert("Record delete Successfully!")</script>')
    print(dbcursor.rowcount,"record deleted")
    
    
else :
    print(dbcursor.etchwarnings(),'-error list')
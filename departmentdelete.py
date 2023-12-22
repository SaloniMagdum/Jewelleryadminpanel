#!C:\Python310-32\python.exe
import cgi
import mysql.connector
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")

form=cgi.FieldStorage()
recordtobedeleted=form.getvalue("id")
#print(recordtobedeleted)
#password=form.getvalue("password")
#mobile=form.getvalue("mobile")


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suraj"
)
if conn.is_connected():
    #print('DB connected')
    dbcursor=conn.cursor()
    
    #print(query)
    dbcursor.execute("DELETE FROM adddepartment WHERE id="+recordtobedeleted)
    
    conn.commit()
    print('<script>alert("Record Deleted Successfully!");window.location="http://127.0.0.1/suraj/pyadmin/Departmentlist.py"</script>')
    
    print(dbcursor.rowcount, "record deleted.")
else :
    print(dbcursor.etchwarnings(),'-error list')
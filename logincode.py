#!C:\Python310-32\python.exe
import cgi
import mysql.connector
print("Content-Type:text/html\n")
import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
Email=form.getvalue("Email")
Password=form.getvalue("Password")
conn=mysql.connector.connect(host="localhost",
user="root", 
password="",
database="suraj"
)
if conn.is_connected():
    print('DB connected')
    dbcursor=conn.cursor()
    query= "INSERT INTO login(Email,Password) VALUES (%s, %s)"
    val=(Email,Password)
    dbcursor.execute(query,val)
    conn.commit()
   
    print('<script>alert("Record Inserted Successfully!")</script>')
    print(dbcursor.rowcount,"record inserted.")

    query="SELECT * FROM login "
    dbcursor.execute(query)
    result=dbcursor.fetchall()
    print('<html><head><style>.content-table thead tr { background-color:darkseagreen; color:green; text-align: left; font-weight:bold;}.content-table{ border-collapse:collapse; margin: 25px 0; font-size: 0.9em; min-width: 400px; border-radius: 5px 5px 0 0; overflow: hidden; box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);}.content-table th, .content-table td{ padding: 12px 15px;}.content-table tbody tr{ border-bottom: 1px solid #dddddd;} .content-table tbody tr:nth-of-type(even){background-color: #f3f3f3;}</style></head><body>')
    print('<style>.content-table thead tr{ "background-color:darkseagreen"; color:green; text-align: left; font-weight:bold;}</style><table class="content-table"><th>Actions </th><th>id</th><th>Email </th><th>Password</th>')
    for x in result:
         print(f'<tr><td><input type="button" value="Edit"  ><br><br><input type="button" value="Delete"></td><td>{x[0]}</td><td>{x[1]}</td><td>{x[2]}</td></tr>')
    print('</table></body></html>')    
else:
      print(dbcursor.etchwarnings(),'-error list')
      
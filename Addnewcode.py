#!C:\Python310-32\python.exe
import cgi
import mysql.connector
print("Content-Type: text/html\n")
import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
Jewelleryname=form.getvalue("Jewelleryname")
Category=form.getvalue("Category")
Weight=form.getvalue("Weight")
Quantity=form.getvalue("Quantity")
Description=form.getvalue("Description")
GST=form.getvalue("GST")
Totalprice=form.getvalue("Totalprice")
Stock=form.getvalue("Stock")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suraj"
)
if conn.is_connected():
    print('Add product Successfully')
    dbcursor=conn.cursor()
    query = "INSERT INTO addnew(Jewelleryname,Category,Weight,Quantity,Description,GST,Totalprice,Stock) VALUES (%s,%s, %s, %s ,%s, %s, %s, %s)"
    val=(Jewelleryname,Category,Weight,Quantity,Description,GST,Totalprice,Stock)
    dbcursor.execute(query,val)
    conn.commit()
    print('<script>alert("Record Inserted Successfully!")</script>')
    print(dbcursor.rowcount,"record inserted")
   
    query="SELECT * FROM addnew"
    dbcursor.execute(query)
    result=dbcursor.fetchall()
    print('<html><head><style>.content-table thead tr { background-color:darkseagreen; color:green; text-align: left; font-weight:bold;}.content-table{ border-collapse:collapse; margin: 25px 0; font-size: 0.9em; min-width: 400px; border-radius: 5px 5px 0 0; overflow: hidden; box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);}.content-table th, .content-table td{ padding: 12px 15px;}.content-table tbody tr{ border-bottom: 1px solid #dddddd;} .content-table tbody tr:nth-of-type(even){background-color: #f3f3f3;}</style></head><body>')
    print('<style>.content-table thead tr{ "background-color:darkseagreen"; color:green; text-align: left; font-weight:bold;}</style><table class="content-table"><th>Actions </th><th>id</th><th>Jewelleryname </th><th>Category</th><th>Weight</th><th>Quantity</th><th>Description</th><th>Totalprice</th><th>Stock</th>')
    for x in result:
               print(f'<tr><td><input type="button" value="Edit" ><br><br><input type="button" value="Delete"></td><td>{x[0]}</td><td>{x[1]}</td><td>{x[2]}</td><td>{x[3]}</td><td>{x[4]}</td><td>{x[5]}</td><td>{x[6]}</td><td>{x[7]}</td><td>{x[8]}</td></tr>')
    print('</table></body></html>')   
    
      
    
else :
    print(dbcursor.etchwarnings(),'-error list')
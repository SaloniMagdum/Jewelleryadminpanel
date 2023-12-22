#!C:\Python310-32\python.exe
import cgi
import mysql.connector
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()

cid=form.getvalue("id")
var1=form.getvalue("Categoryname")
var2=form.getvalue("Description")
var3=form.getvalue("GST")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suraj"
)

dbcursor=conn.cursor()
dbcursor.execute("update addcategory set Categoryname='"+str(var1)+"',Description='"+str(var2)+"',GST='"+str(var3)+"'where id='"+str(cid)+"';")
conn.commit()
    
if dbcursor.rowcount==1:
    form=f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url =categorylist.py" />
        </head>
        <body>
        print('<script>alert("Record update Successfully")</script>')
        </body>
        </html>'''
    print(form)
#else:
 #   form=f'''
  #      <!DOCTYPE html>
   #     <html>
    #    <head>
     #       <title>HTML Meta Tag</title>
      #      <meta http-equiv = "refresh" content = "0; url = categorylist.py" />
       # </head>
        #<body>
        #<script>alert("Something Went Wrong")</script>
        #</body>
        #</html>
         # '''
    #print(form)        

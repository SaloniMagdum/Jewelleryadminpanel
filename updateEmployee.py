#!C:\Python310-32\python.exe
import cgi
import mysql.connector
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()

cid=form.getvalue("id")
var1=form.getvalue("Name")
var2=form.getvalue("Phone")
var3=form.getvalue("Address")
var4=form.getvalue("AdharNo")
var5=form.getvalue("PanNoNo")
var6=form.getvalue("Department")
var7=form.getvalue("AccountNo")


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suraj"
)

dbcursor=conn.cursor()
dbcursor.execute("update addemployee set Name='"+str(var1)+"',Phone='"+str(var2)+"',Address='"+str(var3)+"',AdharNo='"+str(var4)+"',PanNo='"+str(var5)+"',Department='"+str(var6)+"',AccountNo='"+str(var7)+"'where id='"+str(cid)+"';")
conn.commit()
    
if dbcursor.rowcount==1:
    form=f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url =Displayemployee.py" />
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
      #      <meta http-equiv = "refresh" content = "0; url = Displayemployee.py" />
       # </head>
        #<body>
        #<script>alert("Something Went Wrong")</script>
        #</body>
        #</html>
         # '''
    #print(form)        

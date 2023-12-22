#!C:\Python310-32\python.exe
import cgi
import mysql.connector
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()

cid=form.getvalue("id")
var1=form.getvalue("ShopName")
var2=form.getvalue("OwnerName")
var3=form.getvalue("Email")
var4=form.getvalue("Password")
var5=form.getvalue("MobileNo")
var6=form.getvalue("Address")
var7=form.getvalue("AdharNo")
var8=form.getvalue("PanNo")
var9=form.getvalue("Registrationdate")
var10=form.getvalue("Certificationdate")
var11=form.getvalue("Shippingaddress")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suraj"
)

dbcursor=conn.cursor()
dbcursor.execute("update shopdetails set ShopName='"+str(var1)+"',OwnerName='"+str(var2)+"',Email='"+str(var3)+"',Password='"+str(var4)+"',MobileNo='"+str(var5)+"',Address='"+str(var6)+"',AdharNo='"+str(var7)+"',PanNo='"+str(var8)+"',Registrationdate='"+str(var9)+"',Certificationdate='"+str(var10)+"',Shippingaddress='"+str(var11)+"'where id='"+str(cid)+"';")
conn.commit()
    
if dbcursor.rowcount==1:
    form=f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url =shoplist.py" />
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
      #      <meta http-equiv = "refresh" content = "0; url = shoplist.py" />
       # </head>
        #<body>
        #<script>alert("Something Went Wrong")</script>
        #</body>
        #</html>
         # '''
    #print(form)        

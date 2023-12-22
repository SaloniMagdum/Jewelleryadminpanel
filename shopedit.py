#!C:\Python310-32\python.exe
import cgi,requests
import mysql.connector
print("Content-Type: text/html\n")
import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
#id=requests.GET.get('id')

idrec=form.getvalue("id")
print(f'<input readonly value="{idrec}">')
#dbcursor.execute("select * from shopdetails where id='"+idrec")
#result=dbcursor.fetchone()

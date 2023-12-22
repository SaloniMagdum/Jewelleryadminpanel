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
Jewellerynamerec=form.getvalue("Jewelleryname")
print(f'<input readonly value="{Jewellerynamerec}">')
Categoryrec=form.getvalue("Category")
print(f'<input readonly value="{Categoryrec}">')
Weightrec=form.getvalue("Weight")
print(f'<input readonly value="{Weightrec}">')
Quantityrec=form.getvalue("Quantity")
print(f'<input readonly value="{Quantityrec}">')
Descriptionrec=form.getvalue("Description")
print(f'<input readonly value="{Descriptionrec}">')
GSTrec=form.getvalue("GST")
print(f'<input readonly value="{GSTrec}">')
Totalpricerec=form.getvalue("Totalprice")
print(f'<input readonly value="{Totalpricerec}">')
Stockrec=form.getvalue("Stock")
print(f'<input readonly value="{Stockrec}">')



if conn.is_connected():
    dbcursor=conn.cursor()
    query = "update  addnew set Jewelleryname='"+str(Jewelleryname)+"',Category='"+str(Category)+"',Weight='"+str(Weight)+"',Quantity='"+str(Quantity)+"',Description='"+str(Description)+"',GST='"+str(GST)+"',Totalprice='"+str(Totalprice)+"',Stock='"+str(Stock)+"'where id="+str(id)
    
    dbcursor.execute(query)
    conn.commit()
    print('<script>alert("Record Edit Successfully!")</script>')
    print(dbcursor.rowcount,"record upadted")
    
    
else :
    print(dbcursor.etchwarnings(),'-error list')
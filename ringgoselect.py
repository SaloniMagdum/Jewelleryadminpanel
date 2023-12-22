#!C:\Python310-32\python.exe
import cgi
import mysql.connector
print("Content-Type: text/html\n")
import cgi,cgitb
cgitb.enable()
conn=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suraj"
)
if conn.is_connected():
    print('DB connected')
    dbcursor=conn.cursor()
    query="SELECT * FROM addringgold"
    dbcursor.execute(query)
    result=dbcursor.fetchall()
     
    print('<!DOCTYPE html> <html lang="zxx"> <meta http-equiv="content-type" content="text/html;charset=UTF-8" /> ')  
    print('<head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" /> <title>Suraj Jewellers</title>')
    print('<link rel="icon" href="img/suraj.jpeg" type="image/jpeg"> <link rel="stylesheet" href="css/bootstrap1.min.css" /> <link rel="stylesheet" href="vendors/themefy_icon/themify-icons.css" /> <link rel="stylesheet" href="vendors/scroll/scrollable.css" /> <link rel="stylesheet" href="vendors/font_awesome/css/all.min.css" /> <link rel="stylesheet" href="vendors/datatable/css/jquery.dataTables.min.css" /> <link rel="stylesheet" href="vendors/datatable/css/responsive.dataTables.min.css" /> <link rel="stylesheet" href="vendors/datatable/css/buttons.dataTables.min.css" /> <link rel="stylesheet" href="css/metisMenu.css"> <link rel="stylesheet" href="css/style1.css" />')
    print('</head> <body class="crm_body_bg">')
    print('<nav class="sidebar"> <div class="logo d-flex justify-content-between"> <a class="large_logo" href="index.html"><img src="img/suraj.jpeg" alt=""></a> <a class="small_logo" href="index.html"><img src="img/mini_logo.png" alt=""></a> <div class="sidebar_close_icon d-lg-none"> <i class="ti-close"></i></div> </div> <ul id="sidebar_menu"> <li><a href="index.html" aria-expanded="false"> <div class="nav_icon_small"> </div> </a> <ul> <li><a href="data_table.html">Data Tables</a></li> </ul> </li> </nav>')
    print('<section class="main_content dashboard_part large_header_bg"> </li></div></div></div></div></div><div class="main_content_iner "><div class="container-fluid p-0"> <div class="row justify-content-center"> <div class="col-lg-12"> <div class="white_card card_height_100 mb_30"> <div class="white_card_header"> <div class="box_header m-0"> <div class="main-title"> <h3 class="m-0">Data table</h3> </div> </div> </div>')
    print('<div class="white_card_body"> <div class="QA_section"> <div class="white_box_tittle list_header"><h4>Table</h4><div class="box_right d-flex lms_block"><div class="serach_field_2"><div class="search_inner"> <form Active="#"> </form> </div> </div> </div> </div> <div class="QA_table mb_30">')
    print('<table class="table lms_table_active ">')
    print('<thead> <tr> <th scope="col">id</th><th scope="col">Jewelleyname</th><th scope="col">Category</th><th scope="col">Weight</th><th scope="col">Quantity</th><th scope="col">Description</th><th scope="col">GST</th><th scope="col">Totalprice</th><th scope="col">Stock</th>  </tr> </thead>') 
    
    print('<tbody> ')
    for x in result:
        print(f'<tr> <td scope="row">{x[0]}</td><td>{x[1]}</td><td>{x[2]}</td><td>{x[3]}</td><td>{x[4]}</td><td>{x[5]}</td><td>{x[6]}</td><td>{x[7]}</td><td>{x[8]}</td> ')
        print('</tr>')
    print('</tbody></table></div></div></div></div></div><div class="col-12"></div></div></div></div></section>')
    print('<script src="js/jquery1-3.4.1.min.js"></script> <script src="js/popper1.min.js"></script> <script src="js/bootstrap1.min.js"></script> <script src="js/metisMenu.js"></script> <script src="vendors/datatable/js/jquery.dataTables.min.js"></script> <script src="vendors/datatable/js/dataTables.responsive.min.js"></script> <script src="vendors/datatable/js/dataTables.buttons.min.js"></script> <script src="vendors/datatable/js/buttons.flash.min.js"></script> <script src="vendors/datatable/js/jszip.min.js"></script> <script src="vendors/datatable/js/pdfmake.min.js"></script> <script src="vendors/datatable/js/vfs_fonts.js"></script> <script src="vendors/datatable/js/buttons.html5.min.js"></script> <script src="vendors/datatable/js/buttons.print.min.js"></script> <script src="vendors/scroll/perfect-scrollbar.min.js"></script> <script src="vendors/scroll/scrollable-custom.js"></script> <script src="js/custom.js"></script>')
    print('</body> </html>')
    
    
else :
    print(dbcursor.etchwarnings(),'-error list')
	
	
	
	
	
#!"C:\Users\Mohon\AppData\Local\Programs\Python\Python37-32\python.exe"

import cgi, cgitb, os, sys

UPLOAD_DIR = './../img/products'

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1>Data Inserted successfully</h1>")
print("<h1>It works! </h1>")
print("<a href='./../Home/home.py'>Go To Home</a>")

form = cgi.FieldStorage()


if form.getvalue('categories'):
    Categories = form.getvalue('categories')
    alldata = open("alldata.txt","a")
    alldata.write(Categories+";")
    alldata.close()
    print('The string "' + Categories + '" was uploaded successfully')
else:
    print("<h1>You didn't insert the categories</h1>")

if form.getvalue('isbn'):
    ISBN = form.getvalue('isbn')
    alldata = open("alldata.txt","a")
    alldata.write(ISBN+";")
    alldata.close()
    print('The string "' + ISBN + '" was uploaded successfully')
else:
    print("<h1>You didn't insert the ISBN number</h1>")

if form.getvalue('title'):
    Title = form.getvalue('title')
    alldata = open("alldata.txt","a")
    alldata.write(Title+";")
    alldata.close()
    print('The string "' + Title + '" was uploaded successfully')
else:
    print("<h1>You didn't insert title</h1>")

if form.getvalue('author'):
    Author = form.getvalue('author')
    alldata = open("alldata.txt","a")
    alldata.write(Author+";")
    alldata.close()
    print('The string "' + Author + '" was uploaded successfully')
else:
    print("<h1>You didn't insert Author Name</h1>")

if form.getvalue('publisher'):
    Publisher = form.getvalue('publisher')
    alldata = open("alldata.txt","a")
    alldata.write(Publisher+";")
    alldata.close()
    print('The string "' + Publisher + '" was uploaded successfully')
else:
    print("<h1>You didn't insert Publishers Name</h1>")

if form.getvalue('price'):
    Price = form.getvalue('price')
    alldata = open("alldata.txt","a")
    alldata.write(Price+";")
    alldata.close()
    print('The string "' + Price + '" was uploaded successfully')
else:
    print("<h1>You didn't insert the Price for the Book</h1>")

if form.getvalue('quantity'):
    Quantity = form.getvalue('quantity')
    alldata = open("alldata.txt","a")
    alldata.write(Quantity+";")
    alldata.close()
    print('The string "' + Quantity + '" was uploaded successfully')
else:
    print("<h1>You didn't insert the quantity of the Book</h1>")

#for image upload code below :
#uploaded_file_path = os.path.join(UPLOAD_DIR, os.path.basename(form_file.filename))
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('./../img/products/'+fn, 'wb').write(fileitem.file.read())

   #imgfilepath = open("imgfile.txt","a")
   #imgfilepath.write("./../img/products/"+fn+"\n")
   #imgfilepath.close()

   alldata = open("alldata.txt","a")
   alldata.write("./../img/products/"+fn+";\n")
   alldata.close()


   print("The file "+ fn +" was uploaded successfully")

else:
   print("No file was uploaded")
#-----------------------------
#alldata = open("alldata.txt","a")
#alldata.write(Categories+";")
#alldata.close()



cgitb.enable()

print("</body></html>")

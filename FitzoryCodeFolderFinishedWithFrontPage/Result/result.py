#!"C:\Users\Mohon\AppData\Local\Programs\Python\Python37-32\python.exe"

import cgi, cgitb, re

form = cgi.FieldStorage()

print("Content-type:text/html\r\n\r\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='./../css/style.css'>")
print("<link rel='stylesheet' type='text/css' href='./../css/result.css'>")
print("</head>")

print("<body>")

# here we are get the value for searching alldata txt file----------
if form.getvalue('categories'):
    Categories = form.getvalue('categories')
else:
    Categories = 0

if form.getvalue('publishers'):
    Publishers = form.getvalue('publishers')
else:
    Publishers = 0


alldata = open("./../Maintain/alldata.txt","r")

f = open('searchresult.txt', 'r+')
f.truncate(0)


for line in alldata:
    if Publishers == 0 and Categories != 0:
        if re.match(Categories, line):
            searchresult = open("searchresult.txt","a")
            searchresult.write(line)
            searchresult.close()
        else:
            line = "No-Data-Found;"
            searchresult = open("searchresult.txt","a")
            searchresult.write(line)
            searchresult.close()
    elif Categories == 0 and Publishers != 0:
        if re.match(Publishers, line):
            searchresult = open("searchresult.txt","a")
            searchresult.write(line)
            searchresult.close()
        else:
            line = "No-Data-Found;"
            searchresult = open("searchresult.txt","a")
            searchresult.write(line)
            searchresult.close()
    elif Categories != 0 and Publishers != 0:
        if re.match(Categories, line):
            searchresult = open("searchresult.txt","a")
            searchresult.write(line)
            searchresult.close()
        else:
            line = "No-Data-Found;"
            searchresult = open("searchresult.txt","a")
            searchresult.write(line)
            searchresult.close()
    else:
        line = "No-Data-Found;"
        searchresult = open("searchresult.txt","a")
        searchresult.write(line)
        searchresult.close()
# here we are get the value for searching alldata txt file----------


res = open("resultdata.txt","r")
resValue = res.readlines()

print("<div class='fullContainer'>")
print("<!--header-->")
print("<div class='header'>")
print("<h1>"+resValue[0]+"</h1>")
print("</div>")

print("<!--menu-->")
print("<div class='nav'>")
print("<ul>")
print("<li><a href='./../Home/home.py'>Home</a></li>")
print("<li><a href='./../Site/site.py'>Site Map</a></li>")
print("<li><a href='./../Search/search.py'>Catalogue Search</a></li>")
print("<li><a href='./../Result/result.py'>Result</a></li>")
print("<li><a href='./../Maintain/maintain.py'>Maintenance</a></li>")
print("</ul>")
print("</div>")



print("<!-- Main Content Section -->")
print("<div class='mainContent'>")
print("<div class='wrapContent'>")
print("<div class='contentSearchHeader'>")
print("<div class='spacer'></div>")
print("<h2>You Search Result</h2>")
print("<div class='spacer'></div>")
print("<h4>"+resValue[1]+"</h4>")
print("</div>")
print("<div class='spacer'>")

print("</div>")
print("<div class='contentSearchDataTable'>")
print("<table class='center'>")

head = open("tableheader.txt","r")
headerValue = head.readlines()

print("<tr>")

print("<th>"+headerValue[0]+"</th>") #image
print("<th>"+headerValue[1]+"</th>") #Title
print("<th>"+headerValue[2]+"</th>") #ISBN Number
print("<th>"+headerValue[3]+"</th>") #Category
print("<th>"+headerValue[4]+"</th>") #Author(s)/Artist(s)
print("<th>"+headerValue[5]+"</th>") #Publisher
print("<th>"+headerValue[6]+"</th>") #Price
print("<th>"+headerValue[7]+"</th>") #Quantity-on-hand
print("</tr>")



res = open("searchresult.txt","r")
for line in res:
    valueRes = line.split(";")

    print("<tr>")
    print("<td><img src="+valueRes[7]+" alt='book Picture'></td>") #Image
    print("<td>"+valueRes[2]+"</td>") # Title
    print("<td>"+valueRes[1]+"</td>") # ISBN
    print("<td>"+valueRes[0]+"</td>") # category
    print("<td>"+valueRes[3]+"</td>") # Author(s)/Artist(s)
    print("<td>"+valueRes[4]+"</td>") # publisher
    print("<td>"+valueRes[5]+"</td>") # Price
    print("<td>"+valueRes[6]+"</td>") # Quantity
    print("</tr>")
    print("<tr>")



print("</table>")
print("</div>")
print("</div>")
print("</div>")


print("<!--footer-->")
print("<div class='footerResult'>")
print("<p>"+resValue[2]+" <b>"+resValue[3]+"</b>.</p>")
print("</div>")

print("</div>")
print("</body>")
print("</html>")

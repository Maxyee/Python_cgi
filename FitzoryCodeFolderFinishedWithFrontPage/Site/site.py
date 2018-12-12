#!"C:\Users\Mohon\AppData\Local\Programs\Python\Python37-32\python.exe"

print("Content-type:text/html\r\n\r\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='./../css/style.css'>")
print("<link rel='stylesheet' href='./../css/site.css' type='text/css'>")
print("</head>")

print("<body>")

print("<div class='fullContainer'>")
print("<!--header-->")
print("<div class='header'>")
print("<h1>Fitzory Catholic Bookshop</h1>")
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
print("<div class='spacer'>")

print("</div>")

print("<div class='siteHeader'>")

site = open("sitedata.txt","r")
siteValue = site.readlines()


print("<p>"+siteValue[0]+"</p>")
print("</div>")
print("<div class='spacer'>")

print("</div>")
print("<div class='linkContent'>")
print("<div class='spacer'>")

print("</div>")

print("<div class='showDataBox'>")
print("<div class='sidesection'>")

print("<div class='categories'>")
print("<h3>Categories</h3>")

cat = open("./../Maintain/category.txt","r")
value = cat.readlines()


print("<div class='sidenav'>")
for x in value:
    print("<p>"+ x +"</p>")

print("</div>")
print("</div>")


print("<div class='publishers'>")

pub = open("./../Maintain/publishers.txt","r")
pubValue = pub.readlines()

print("<h3>Publishers</h3>")
print("<div class='sidenav'>")

for y in pubValue:
    print("<p>"+ y +"</p>")

print("</div>")
print("</div>")
print("</div>")

print("</div>")


print("<div class='showDataBox'>")
print("<div class='collectionphoto'>")
print("<div class='dataBoxHeader'>")
print("<p>"+siteValue[1]+"</p>")
print("</div>")

print("<div class='spacer'>")

print("</div>")

print("<!-- First Row Of Box -->")
data = open("./../Maintain/alldata.txt","r")

for aline in data:
    values = aline.split(";")
    print("<div class='dataBoxMainSection'>")



    print("<div class='Mainbox'>")
    print("<div class='boxHeader'>")
    print("<p>Category--"+values[0]+"</p>")
    print("</div>")
    print("<div class='boxContent'>")
    print("<img src="+values[7]+"  alt=''>")
    print("<p class='boxContentDescription'>Title--"+values[2]+"</p>")
    print("<p class='boxContentDescription'>ISBN--"+values[1]+"</p>")
    print("<p class='boxContentDescription'>Price--"+values[5]+"</p>")
    print("<p>Details</p>")
    print("</div>")

    print("</div>")


print("</div>")


print("</div>")
print("</div>")
print("</div>")
print("</div>")


print("<!--footer-->")
print("<div class='footerSite'>")
print("<p>"+siteValue[2]+" <b>"+siteValue[3]+"</b>.</p>")
print("</div>")

print("</div>")
print("</body>")
print("</html>")

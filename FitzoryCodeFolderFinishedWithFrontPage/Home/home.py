#!"C:\Users\Mohon\AppData\Local\Programs\Python\Python37-32\python.exe"


print("Content-type:text/html\r\n\r\n")
print("<!DOCTYPE html")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='./../css/style.css'>")
print("<link rel='stylesheet' href='./../css/home.css' type='text/css'>")
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



f = open("homedata.txt","r")
f1 = f.readlines()



print("<div class='contentHeader'>")
print("<h2>"+f1[0]+"</h2>")
print("</div>")

print("<div class='spacer'>")

print("</div>")

print("<div class='contentDescription'>")
print("<h3>"+f1[1]+"</h3>")
print("</div>")

print("<div class='spacer'>")

print("</div>")

print("<div class='companyLogo'>")
print("<img src="+f1[2]+" alt='logo' style='width:100%;'/>")
print("</div>")

print("<div class='spacer'>")

print("</div>")

print("<div class='companyDescription'>")
print("<p>")
print(""+f1[3]+"")
print(""+f1[4]+"")
print(""+f1[5]+"")
print("</p>")
print("</div>")
print("</div>")
print("</div>")


print("<!--footer-->")
print("<div class='footer'>")
print("<p>"+f1[6]+" <b>"+f1[7]+"</b>.</p>")
print("</div>")

print("</div>")
print("</body>")
print("</html>")

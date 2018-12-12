#!"C:\Users\Mohon\AppData\Local\Programs\Python\Python37-32\python.exe"

print("Content-type:text/html\r\n\r\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='./../css/style.css'>")
print("<link rel='stylesheet' href='./../css/search.css' type='text/css'>")
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

search = open("searchdata.txt","r")
searchValue = search.readlines()

print("</div>")
print("<div class='searchpageHeader'>")
print("<p>"+searchValue[0]+"</p>")
print("</div>")
print("<div class='spacer'>")

print("</div>")
print("<div class='searchBox'>")
#add from here ------
print("<form action='./../Result/result.py' method='post'>")
print("<table class='center'>")
print("<tr>")
print("<td>Categories</td>")
print("<td><input type='text' name='categories'/></td>")
print("</tr>")
print("<tr>")
print("<td>Publishers</td>")
print("<td><input type='text' name='publishers'/></td>")
print("</tr>")
print("<tr>")
#print("<td>Price</td>")
#print("<td><input type='text' name='price'/></td>")
print("</tr>")
print("<tr>")
print("<td></td>")
print("<td><button type='submit'>Search</button></td>")
print("</tr>")

print("</table>")
print("</form>")
#end from here ---------
print("</div>")
print("</div>")
print("</div>")


print("<!--footer-->")
print("<div class='footer'>")
print("<p>"+searchValue[1]+" <b>"+searchValue[2]+"</b>.</p>")
print("</div>")

print("</div>")
print("</body>")
print("</html>")

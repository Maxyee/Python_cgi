#!"C:\Users\Mohon\AppData\Local\Programs\Python\Python37-32\python.exe"

print("Content-type:text/html\r\n\r\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='./../css/style.css'>")
print("<link rel='stylesheet' type='text/css' href='./../css/result.css'>")
print("</head>")

print("<body>")



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
print("<th>"+headerValue[0]+"</th>")
print("<th>"+headerValue[1]+"</th>")
print("<th>"+headerValue[2]+"</th>")
print("<th>"+headerValue[3]+"</th>")
print("<th>"+headerValue[4]+"</th>")
print("<th>"+headerValue[5]+"</th>")
print("<th>"+headerValue[6]+"</th>")
print("<th>"+headerValue[7]+"</th>")
print("<th>"+headerValue[8]+"</th>")
print("</tr>")

tab = open("table.txt","r")
tabValue = tab.readlines()

print("<tr>")
print("<td>"+tabValue[0]+"</td>")
print("<td><img src="+tabValue[1]+" alt='book Picture'></td>")
print("<td>"+tabValue[2]+"</td>")
print("<td>"+tabValue[3]+"</td>")
print("<td>"+tabValue[4]+"</td>")
print("<td>"+tabValue[5]+"</td>")
print("<td>"+tabValue[6]+"</td>")
print("<td>"+tabValue[7]+"</td>")
print("<td>"+tabValue[8]+"</td>")
print("</tr>")
print("<tr>")
print("<td>"+tabValue[9]+"</td>")
print("<td><img src="+tabValue[10]+" alt='book Picture'></td>")
print("<td>"+tabValue[11]+"</td>")
print("<td>"+tabValue[12]+"</td>")
print("<td>"+tabValue[13]+"</td>")
print("<td>"+tabValue[14]+"</td>")
print("<td>"+tabValue[15]+"</td>")
print("<td>"+tabValue[16]+"</td>")
print("<td>"+tabValue[17]+"</td>")
print("</tr>")
print("<tr>")
print("<td>"+tabValue[18]+"</td>")
print("<td><img src="+tabValue[19]+" alt='book Picture'></td>")
print("<td>"+tabValue[20]+"</td>")
print("<td>"+tabValue[21]+"</td>")
print("<td>"+tabValue[22]+"</td>")
print("<td>"+tabValue[23]+"</td>")
print("<td>"+tabValue[24]+"</td>")
print("<td>"+tabValue[25]+"</td>")
print("<td>"+tabValue[26]+"</td>")
print("</tr>")
print("<tr>")
print("<td>"+tabValue[27]+"</td>")
print("<td><img src="+tabValue[28]+" alt='book Picture'></td>")
print("<td>"+tabValue[29]+"</td>")
print("<td>"+tabValue[30]+"</td>")
print("<td>"+tabValue[31]+"</td>")
print("<td>"+tabValue[32]+"</td>")
print("<td>"+tabValue[33]+"</td>")
print("<td>"+tabValue[34]+"</td>")
print("<td>"+tabValue[35]+"</td>")
print("</tr>")
print("<tr>")
print("<td>"+tabValue[36]+"</td>")
print("<td><img src="+tabValue[37]+" alt='book Picture'></td>")
print("<td>"+tabValue[38]+"</td>")
print("<td>"+tabValue[39]+"</td>")
print("<td>"+tabValue[40]+"</td>")
print("<td>"+tabValue[41]+"</td>")
print("<td>"+tabValue[42]+"</td>")
print("<td>"+tabValue[43]+"</td>")
print("<td>"+tabValue[44]+"</td>")
print("</tr>")
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
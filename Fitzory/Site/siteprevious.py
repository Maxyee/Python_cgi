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
    print("<a href='site.py'>"+ x +"</a>")
print("</div>")
print("</div>")


print("<div class='publishers'>")

pub = open("./../Maintain/publishers.txt","r")
pubValue = pub.readlines()

print("<h3>Publishers</h3>")
print("<div class='sidenav'>")

for y in pubValue:
        print("<a href='site.py'>"+y+"</a>")

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
print("<div class='dataBoxMainSection'>")




print("<div class='Mainbox'>")

print("<div class='boxHeader'>")

title = open("./../Maintain/title.txt","r")
titleValue = title.readlines()

for tit in titleValue:
    print("<p>"+tit+"</p>")
print("</div>")


print("<div class='boxContent'>")

img = open("./../Maintain/imgfile.txt","r")
imgsrc = img.readlines()

for ima in imgsrc:
    print("<img src="+ima+">")


author = open("./../Maintain/author.txt","r")
auth = author.readlines()

for au in auth:
    print("<p class='boxContentDescription'>"+au+"</p>")

isbn = open("./../Maintain/isbn.txt","r")
isb = isbn.readlines()

for isvalue in isb:
    print("<p class='boxContentDescription'>"+isvalue+"</p>")

price = open("./../Maintain/price.txt","r")
pri = price.readlines()

for pr in pri:
    print("<p class='boxContentDescription'>"+pr+"</p>")
print("<button>Details</button>")
print("</div>")

print("</div>")

print("<div class='Mainbox'>")

print("<div class='boxHeader'>")
print("<p>"+bookinfoValue[3]+"</p>")
print("</div>")

print("<div class='boxContent'>")
print("<img src="+bookinfoValue[4]+" alt=''>")
print("<p class='boxContentDescription'>"+bookinfoValue[5]+"</p>")
print("<button>Details</button>")
print("</div>")

print("</div>")

print("<div class='Mainbox'>")

print("<div class='boxHeader'>")
print("<p>"+bookinfoValue[6]+"</p>")
print("</div>")

print("<div class='boxContent'>")
print("<img src="+bookinfoValue[7]+" alt=''>")
print("<p class='boxContentDescription'>"+bookinfoValue[8]+"</p>")
print("<button>Details</button>")
print("</div>")

print("</div>")

print("<div class='Mainbox'>")

print("<div class='boxHeader'>")
print("<p>"+bookinfoValue[9]+"</p>")
print("</div>")

print("<div class='boxContent'>")
print("<img src="+bookinfoValue[10]+" alt=''>")
print("<p class='boxContentDescription'>"+bookinfoValue[11]+"</p>")
print("<button>Details</button>")
print("</div>")

print("</div>")
print("</div>")

print("<!-- Secound Row of the Box -->")
print("<div class='dataBoxMainSection2'>")
print("<div class='Mainbox'>")

print("<div class='boxHeader'>")
print("<p>"+bookinfoValue[12]+"</p>")
print("</div>")

print("<div class='boxContent'>")
print("<img src="+bookinfoValue[13]+" alt=''>")
print("<p class='boxContentDescription'>"+bookinfoValue[14]+"</p>")
print("<button>Details</button>")
print("</div>")

print("</div>")

print("<div class='Mainbox'>")

print("<div class='boxHeader'>")
print("<p>"+bookinfoValue[15]+"</p>")
print("</div>")

print("<div class='boxContent'>")
print("<img src="+bookinfoValue[16]+" alt=''>")
print("<p class='boxContentDescription'>"+bookinfoValue[17]+"</p>")
print("<button>Details</button>")
print("</div>")

print("</div>")

print("<div class='Mainbox'>")

print("<div class='boxHeader'>")
print("<p>"+bookinfoValue[18]+"</p>")
print("</div>")

print("<div class='boxContent'>")
print("<img src="+bookinfoValue[19]+" alt=''>")
print("<p class='boxContentDescription'>"+bookinfoValue[20]+"</p>")
print("<button>Details</button>")
print("</div>")

print("</div>")

print("<div class='Mainbox'>")

print("<div class='boxHeader'>")
print("<p>"+bookinfoValue[21]+"</p>")
print("</div>")

print("<div class='boxContent'>")
print("<img src="+bookinfoValue[22]+" alt=''>")
print("<p class='boxContentDescription'>"+bookinfoValue[23]+"</p>")
print("<button>Details</button>")
print("</div>")

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

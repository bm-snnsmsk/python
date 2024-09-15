from bs4 import BeautifulSoup

# pip install BeautifulSoup
# pip install beautifulsoup4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>sinan</h1>
    <h1>sinan</h1>


   <div class="bir">  <ul>
        <li>snn 1234 </li>
        <li>snn 1234 </li>
        <li>snn 1234 </li>
        <li>snn 1234 </li>
        <li>snn 1234 </li>
    </ul></div>

<div class="iki">
    
    <ul>
        <li>a1</li>
        <li>a1</li>
        <li>a1</li>
        <li>a1</li>
        <li>a1</li>
    </ul> </div>

<div class="uc">
    
    <ul>
        <li>snn 33333 </li>
        <li>snn 33333 </li>
        <li>snn 33333 </li>
        <li>snn 33333 </li>
        <li>snn 33333 </li>
    </ul> </div>

    <a id="abir" href="http://google.com">Google</a>
    <a href="http://youtube.com">Youtube</a>
    <a class="sinifuc" href="http://meb.gov.tr">MEB</a>


</body>
</html>

'''
soup = BeautifulSoup(html_doc, "html.parser")

# result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name
result = soup.title.string

result = soup.h1    # ilk h1'i alır
result = soup.h1.name
result = soup.h1.string

result = soup.find_all("h1") # [<h1>sinan</h1>, <h1>sinan</h1>]
result = soup.find_all("h1")[0] 
result = soup.find_all("h1")[0].string 

result = soup.find_all("div")
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren()
result = soup.div.findNextSibling()
result = soup.div.findNextSibling().findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.find_all("a")
result = soup.a
result = soup.find(id="abir")

# for i in result :
#     print(i.get("href"))





print(result)



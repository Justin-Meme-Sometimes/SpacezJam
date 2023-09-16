from bs4 import BeautifulSoup
import requests
import re
import json
i = 10
overallScript = ""
for i in range(0, 4):
    html_page = requests.get(
        'https://esahubble.org/images/page/' + str(i) + '/')
    soup = BeautifulSoup(html_page.text, 'html.parser')
    # element = soup.find("div", {"id": "content"})
    # element.findChildren()
    script = soup.find("script")
    # print(script.text)
    overallScript = overallScript + script.text
l = []
# print(script.text.split())
j = []
line = overallScript.splitlines()
for i in range(len(line)):
    title = ""
    img = ""
    if "title" in line[i]:
        line[i] = line[i] = line[i][line[i].find("'") + 1:line[i].find(",")-1]
        j.append(line[i])
    if "src" in line[i]:
        line[i] = line[i][line[i].find("'") + 1:line[i].find(",")-1]
        l.append(str(line[i]))
print(len(j), len(l))
x = []
for i in range(len(j)):
    x.append([j[i], l[i]])
print(x)

# Check if a match was found

# print(script)
# print(element)
# img = img.nextSibling.nextSibling
# image = img.findAll('img')
# print(image)

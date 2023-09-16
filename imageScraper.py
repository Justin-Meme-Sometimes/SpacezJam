from bs4 import BeautifulSoup
import requests
import re
import json
import csv
from PIL import Image
import os
i = 5
overallScript = ""
for i in range(0, 40):
    html_page = requests.get(
        'https://esahubble.org/images/page/' + str(i) + '/')
    soup = BeautifulSoup(html_page.text, 'html.parser')
    script = soup.find("script")
    overallScript = overallScript + script.text
l = []
j = []
line = overallScript.splitlines()
for i in range(len(line)):
    title = ""
    img = ""
    if "title" in line[i]:
        line[i] = line[i] = line[i][line[i].find("'") + 1:line[i].find(",")-1]
        if "?" in line[i]:
            line[i] = line[i].replace("?", "")
        if "/" in line[i]:
            line[i] = line[i].replace("/", "")
        j.append([line[i]])
    if "src" in line[i]:
        line[i] = line[i][line[i].find("'") + 1:line[i].find(",")-1]
        l.append(str(line[i]))
# print(len(j), len(l))
train = j[:1400]
test = j[1400:]
for i in range(len(l)):
    img = Image.open(requests.get(l[i], stream=True).raw)
    # path = "../exoFinder/Images"
    # img.save(path + "/" + j[i]+".jpg")


def createCSV(array, csvFile):

    csv_file_path = csvFile

    # Write the data to the CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

    # Write the data rows
        writer.writerows(array)
        print("complete")


def DeleteFiles(directory):
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        print(directory)
        try:
            if os.path.isfile(f):
                os.unlink(file)
        except Exception as e:
            print('Failed to delete %s, Reason: %s' % (file, e))


createCSV(train, "train.csv")
createCSV(test, "test.csv")

# ListFiles('C:/Users/justi/OneDrive/Documents/GitHub/exoFinder/Images')

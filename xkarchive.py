import os
import re
import requests
from bs4 import BeautifulSoup

def downloadHTML(comicNumber):
    r = requests.get('https://xkcd.com/' + str(comicNumber) + '/')
    return r.text

def downloadComic(comicNumber, path):
    print('Download Comic: #' + str(comicNumber))
    regex = r'(https:\/\/imgs\.xkcd\.com\/comics\/)(.*)'
    html = downloadHTML(comicNumber)
    imgURL = soupHTML(html)
    downloadPath = getPath(path)
    title = re.findall(regex, str(imgURL[0]))
    with open(downloadPath + '/' + str(comicNumber) + ' - ' + title[0][1], 'wb') as f:
        image = requests.get(imgURL[0])
        f.write(image.content)

def soupHTML(html):
    soup = BeautifulSoup(html, features="html.parser")
    imgURL = soup.find_all('img')
    return 'https:' + str(imgURL[1]['src']), 

def getPath(path):
    if os.path.exists(os.path.normpath(path)):
        pass
    else:
        os.mkdir(os.path.normpath(path))

    return (os.path.normpath(path))

def download(latestXKCD, latestDownloadedXKCD, path):
    for x in range(latestDownloadedXKCD, latestXKCD):
        print(x)
        try:
            downloadComic(x, path)
        except:
            print('Some error occured')

def main():
    latestDownloadedXKCD = int(input('Enter the latest XKCD you downloaded. If you do not have any XKCD, please enter 1. \n'))
    latestXKCD = int(input('Please enter the latest XKCD: \n'))
    path = input('Please enter the download path: \n')
    download(latestXKCD, latestDownloadedXKCD, path)

if __name__ == '__main__':
    main()
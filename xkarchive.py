import os
import re
import requests
from bs4 import BeautifulSoup

def downloadHTML(comicNumber):
    '''
    Downloads the HTML side to later grep the image url out of there.
    '''
    r = requests.get('https://xkcd.com/' + str(comicNumber) + '/')
    return r.text

def downloadComic(comicNumber, downloadPath):
    '''
    Downloads the comics and saves it to the disk.
    Uses regex to filter the filename from the URL.
    '''
    print('Download Comic: #' + str(comicNumber))
    regex = r'(https:\/\/imgs\.xkcd\.com\/comics\/)(.*)'
    html = downloadHTML(comicNumber)
    imgURL = soupHTML(html)
    title = re.findall(regex, str(imgURL[0]))
    with open(downloadPath + '/' + str(comicNumber) + ' - ' + title[0][1], 'wb') as f:
        image = requests.get(imgURL[0])
        f.write(image.content)

def soupHTML(html):
    '''
    Finds the image url in the HTML gotten from downloadHTML().
    '''
    soup = BeautifulSoup(html, features="html.parser")
    imgURL = soup.find_all('img')
    return 'https:' + str(imgURL[1]['src']), 

def getPath(path):
    '''
    Checks if the path exists, if not it will create a new folder at this postion.
    '''
    if os.path.exists(os.path.normpath(path)):
        print('Download path exists!')
    else:
        os.mkdir(os.path.normpath(path))
        print('Download path was created!')

    return (os.path.normpath(path))

def download(latestXKCD, latestDownloadedXKCD, path):
    '''
    Triggers the loop to download the XKCD comics.
    '''
    for x in range(latestDownloadedXKCD, latestXKCD):
        print(x)
        # This try statement is caused by: https://xkcd.com/404/
        try:
            downloadComic(x, path)
        except:
            print('Some error occured')

def main():
    latestDownloadedXKCD = int(input('Enter the latest XKCD you downloaded. If you do not have any XKCD, please enter 1. \n'))
    latestXKCD = int(input('Please enter the latest XKCD: \n')) + 1
    path = input('Please enter the download path: \n')
    downloadPath = getPath(path)
    download(latestXKCD, latestDownloadedXKCD, downloadPath)

if __name__ == '__main__':
    main()
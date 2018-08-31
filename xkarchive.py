import os
import re
import requests

def downloadJSON(comicNumber):
    '''
    Downloads the JSON from xkcd.
    '''
    r = requests.get('https://xkcd.com/' + str(comicNumber) + '/info.0.json')
    return r.json()['img']

def downloadComic(comicNumber, downloadPath):
    '''
    Downloads the comics and saves it to the disk.
    Uses regex to filter the filename from the URL.
    '''
    print('Download Comic: #' + str(comicNumber))
    regex = r'(https:\/\/imgs\.xkcd\.com\/comics\/)(.*)'
    img = downloadJSON(comicNumber)
    title = re.findall(regex, img)
    with open(downloadPath + '/' + str(comicNumber) + ' - ' + title[0][1], 'wb') as f:
        image = requests.get(img)
        f.write(image.content)

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
        # This try statement is caused by: https://xkcd.com/404/
        try:
            downloadComic(x, path)
        except:
            print('An error occured:')
            pass

def main():
    latestDownloadedXKCD = int(input('Enter the latest XKCD you downloaded. If you do not have any XKCD, please enter 1. \n'))
    latestXKCD = int(input('Please enter the latest XKCD: \n')) + 1
    path = input('Please enter t^he download path: \n')
    downloadPath = getPath(path)
    download(latestXKCD, latestDownloadedXKCD, downloadPath)

if __name__ == '__main__':
    main()
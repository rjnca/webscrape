from bs4 import BeautifulSoup
import requests
import smtplib


def savecurrentversion(newversion):
    with open('CurrentVersion.txt', 'w') as f:
        f.write(newversion)
    return


def sendupdatemail(newversion):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('raymondrj@gmail.com', 'xteappsxeazkdeeh')
        subject = 'Zii Has Been Updated'
        body = 'Please go to https://free.appnee.com/adobe-zii/ in order to download the latest version of Zii.'

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail('raymondrj@gmail.com', 'raymondrj@gmail.com', msg)
    savecurrentversion(newversion)
    return


def checkversion():
    with open('CurrentVersion.txt') as f:
        fileversion = f.read()

    source = requests.get('https://free.appnee.com/adobe-zii/').text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('article')
    pageversion = article.h1.text
    if pageversion != fileversion:
        sendupdatemail(pageversion)


checkversion()

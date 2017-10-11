#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
import re

ReadUrl = 'http://zlo.rt.mipt.ru/?read='

def GetPost(n):

    url = ReadUrl + str(n)
    page = requests.get(url)

    detect_text = "Это сообщение не существует или введено неправильно"
    soup = BeautifulSoup(page.content, "lxml")

    if soup.find(text = detect_text) != None:
        return None

    return soup

def GetPostDate(n, soup):
    """return a tuple (day, month, year)"""

    msg = soup.find('span', id='m' + str(n))
    if msg == None:
        return None

    # this is different for x.mipt.cc!
    regex = r" \([^)]*\) - (\d+\/\d+\/\d+ \d+:\d+)"
    m = re.match(regex, msg.contents[-1].string)
    if m == None:
        return None

    return int(time.mktime(time.strptime(m.group(1), "%d/%m/%Y %H:%M")))

def main():

    start = 1
    end = 9522068
    stride = 10000

    fdb = open("output.db.txt", "a", buffering = 1)
    fnone = open("none.db.txt", "a", buffering = 1)

    for n in range (start, end, stride):

        soup = GetPost(n)
        if soup == None:
            continue

        epoch = GetPostDate(n, soup)

        if epoch != None:
            fdb.write("{}\t{}\n".format(n, epoch))
        else:
            fnone.write(str(n))


if __name__ == '__main__':
    main()

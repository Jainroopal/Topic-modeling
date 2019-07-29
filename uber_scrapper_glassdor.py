# -*- coding: utf-8 -*-

from urllib.request import urlopen , Request
from bs4 import BeautifulSoup
import re

hdr = {'User-Agent': 'Mozilla/5.0'}
cons_list =[]
pros_list =[]
for i in range(1, 217):
    url = 'https://www.glassdoor.co.in/Reviews/Uber-Reviews-E575263_P'+str(i)+'.htm'
    req = Request(url,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    scr = soup.findAll('script')
    cons_pattern = re.compile('"cons":"(.*?)"')
    cons_list += re.findall(cons_pattern, scr[22].text)
    print(len(cons_list))
    pros_pattern = re.compile('"pros":"(.*?)"')
    pros_list += re.findall(pros_pattern, scr[22].text)
    print(len(pros_list))

import pandas as pd
total = [cons_list, pros_list]
final = list(map(list, zip(*total)))
data = pd.DataFrame(final, columns=('cons', 'pros'))
data.to_csv("uber_data.csv")

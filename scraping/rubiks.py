import os
import re
from datetime import datetime
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str
from classes.UrlManager import url_request

regex = re.compile(r'^(\w+)\.?\s(\d+)(?:\s-\s(?:\w+\.?\s)?\d+)?,\s(\d+)$')

def extract_rubiks_wr(**kwargs) -> str:
    
    parser: HTMLParser = kwargs['parser']
    
    trs = parser.css('table tbody tr')[1:-1]
    del trs[14:19]
    
    data = []
    
    for i, tr in enumerate(trs):
        modifier = i%2
        tds = tr.css('td')
        
        # Discipline
        if not modifier: discipline = format_long_str(tds[0].text())
        
        time = format_str(tds[2-modifier].text())
        player = format_str(tds[3-modifier].text())
        player = re.sub(r'\s(\(.+\))', '', player)
        player = re.sub(r'\s{2,}', ' ', player)
        country = tds[3-modifier].css_first("a:has(img)").attrs["title"]
        
        # Date
        url_date = tds[-1].css_first('a').attrs['href']
        parser_2 = url_request(kwargs['session'], url_date)
        date = parser_2.css_first('div.competition-info dd:first-of-type').text().strip()
        date = re.sub(regex, r'\2 \1 \3', date)
        date = datetime.strptime(date, "%d %b %Y").strftime("%d %B %Y")
        
        data.append(f'{discipline},{time},{player},{country},{date}\n')
        
    data[0:2], data[2:4] = data[2:4], data[0:2]
    data_single = ''.join(data[::2])
    data_average = ''.join(data[1::2])
    
    return data_single + '--\n' + data_average

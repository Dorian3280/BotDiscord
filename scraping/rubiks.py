import os
import re
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str
from classes.UrlManager import url_request


def extract_rubiks_wr(parser: HTMLParser, **kwargs) -> str:
    print(kwargs)
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
        player = re.sub(r'(\(.+\))', '', player)
        player = re.sub(r'\s{2,}', ' ', player)
        country = tds[3-modifier].css_first("a:has(img)").attrs["title"]
        
        # Date
        url_date = tds[-1].css_first('a').attrs['href']
        parser_2 = url_request(kwargs['session'], url_date)
        date = format_str(parser_2.css_first('div.competition-info dd:first-of-type').text())
        print(date)
        
        data.append(f'{discipline},{time},{player},{country}\n')
        
    data[0:2], data[2:4] = data[2:4], data[0:2]
    data_single = ''.join(data[::2])
    data_average = ''.join(data[1::2])
    
    return data_single + '--\n' + data_average

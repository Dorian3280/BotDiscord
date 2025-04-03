import re
from datetime import datetime
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str
from classes.UrlManager import url_request

regex = re.compile(r'(\d{4})\s\((\d+)(?:-\d+)?\s(\w+)\)?', re.I)

def extract_rubiks_wr(**kwargs) -> str:
    
    parser: HTMLParser = kwargs['parser']
    
    trs = parser.css('table tbody tr')[1:-1]
    
    data = []
    b = False
    
    for i, tr in enumerate(trs):
        tds = tr.css('td')
        
        # Discipline
        if not b:
            discipline = format_long_str(tds[0].text())
            rowspan = int(tds[0].attributes["rowspan"])
            b = True
        
        time = format_str(tds[2-b].text())
        player = format_str(tds[3-b].text())
        player = re.sub(r'\s(\(.+\))', '', player)
        player = re.sub(r'\s{2,}', ' ', player)
        country = tds[3-b].css_first("a:has(img)").attrs["title"]
        
        # Date
        date = format_str(tds[4-b].text())
        date = re.search(regex, date)
        
        if date:
            date = f"{date.group(2)} {date.group(3)} {date.group(1)}"
            date = datetime.strptime(date, "%d %B %Y").strftime("%d %b %Y")
        else:
            date = '-'
        
        rowspan -= 1
        b = bool(rowspan)
        data.append(f'{discipline},{time},{player},{country},{date}\n')
        
    data[0:2], data[2:4] = data[2:4], data[0:2]
    data_single = ''.join(data[::2])
    data_average = ''.join(data[1::2])
    
    return data_single + '--\n' + data_average

import re
from datetime import datetime
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str

regex = re.compile(r'(\d{4})\s\((\d+)(?:[-–]\d+)?\s(\w+)\)?', re.I)

def extract_rubiks_wr(**kwargs) -> str:
    
    parser: HTMLParser = kwargs['parser']
    
    trs = parser.css('table tbody tr')[1:-1]
    
    data = []
    rowspan_bool = False
    player_rowspan_bool = False
    type_count = 0
    
    for i, tr in enumerate(trs):
        tds = tr.css('td')

        # Discipline
        if not rowspan_bool:
            rowspan = int(tds[0].attributes["rowspan"])
            discipline = format_long_str(tds[0].text())

        if not type_count:
            type_count = int(tds[1 - rowspan_bool].attributes.get("rowspan", 0))
            type_ = format_str(tds[1 - rowspan_bool].text())
        
            time = format_str(tds[2-rowspan_bool].text())
            
            if not player_rowspan_bool:
                player = format_str(tds[3-rowspan_bool].text())
                player = re.sub(r'\s(\(.+\))', '', player)
                player = re.sub(r'\s{2,}', ' ', player)
                country = tds[3-rowspan_bool].css_first("a").attrs["title"]
            
            # Date
            date = format_str(tds[4-rowspan_bool-player_rowspan_bool].text())
            date = re.search(regex, date)
            
            if date:
                date = f"{date.group(2)} {date.group(3)} {date.group(1)}"
                date = datetime.strptime(date, "%d %B %Y").strftime("%d %b %Y")
            else:
                date = '-'
            
            data.append(f'{type_} {discipline},{time},{player},{country},{date}\n')
        
            if "rowspan" in tds[3-rowspan_bool].attributes:
                player_rowspan_bool = True
        
        if type_count:
            type_count -= 1

        rowspan -= 1
        rowspan_bool = bool(rowspan)

        if not rowspan:
            player_rowspan_bool = False
        
    data[0:2], data[2:4] = data[2:4], data[0:2]
    data_single = ''.join(data[::2])
    data_average = ''.join(data[1::2])
    
    return data_single + '--\n' + data_average

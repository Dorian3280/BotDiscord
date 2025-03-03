import re
from datetime import datetime
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str


def extract_athletics_wr(**kwargs) -> str:

    parser: HTMLParser = kwargs['parser']
    
    data = ''

    for gender in ['Men', 'Women']:
        for performance in parser.css_first(f"h3[id={gender}]").parent.next.next.css('table tbody tr'):
            tds = performance.css('td')
        
            # Multiple lines problem
            if len(tds) != 15: continue
            
            # Discipline
            discipline = format_long_str(tds[0].text(separator=" "))
            discipline = re.sub(r'\s+', ' ', discipline)
            
            # Time
            time = format_str(tds[1].text())
            
            # Player
            players = tds[6].css('a')
            player = format_str(players[0].text()) + (" ..." if len(players) > 1 else '')
            
            # Country
            country = tds[7].css_first("a").attrs["title"]
            
            # Date
            date = format_str(tds[8].text())
            for _format in ["%d %b %Y", "%d %B %Y"]:
                try:
                    date = datetime.strptime(date, _format).strftime("%d %b %Y")
                    break
                except ValueError:
                    continue
            
            data += f'{discipline},{time},{player},{country},{date}\n'
        
        data += '--\n'
        
    return data
    
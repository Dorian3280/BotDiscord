import os
from datetime import datetime
import re
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str


def extract_athletics_wr(parser: HTMLParser) -> str:

    data = ''

    for gender in ['Men', 'Women']:
        for performance in parser.css_first(f"h3[id={gender}]").parent.next.next.css('table tbody tr'):
            tds = performance.css('td')
        
            # Multiple lines problem
            if len(tds) != 15: continue
            
            # Discipline
            discipline = format_long_str(tds[0].text(separator=" "))
            discipline = discipline.replace('[ b ]', '').strip()
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
            date = datetime.strptime(date, "%d %b %Y").strftime("%d %B %Y")
            
            data += f'{discipline},{time},{player},{country},{date}\n'
        
        data += '--\n'
        
    
    return data
    
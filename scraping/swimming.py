import re
import os
from datetime import datetime
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str


def extract_swimming_wr(**kwargs) -> str:
    
    parser: HTMLParser = kwargs['parser']

    data = ''
    
    for h3 in parser.css(f"h3[id=Men], h3[id=Men_2], h3[id=Women], h3[id=Women_2]"):
        for tr in h3.parent.next.next.css('table tbody tr:not(:first-child)'):
            tds = tr.css('td')
            
            # Discipline
            discipline = format_long_str(tds[0].text(separator=" "))
            
            # Time
            time = format_str(tds[1].text())
            
            # Player
            players = tds[3].css('a')
            player = format_str(players[0].text()) + (" ..." if len(players) > 1 else '')
            
            # Country
            country = format_str(tds[4].text())
            
            # Date
            date = format_str(tds[5].text())
            date = datetime.strptime(date, "%d %B %Y").strftime("%d %B %Y")
            
            data += f'{discipline},{time},{player},{country},{date}\n'
        
        data += '--\n'
    
    return data
import re
from datetime import datetime
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str


def extract_athletics_wr(**kwargs) -> str:

    parser: HTMLParser = kwargs['parser']
    
    data = ''
    rowspan_bool = False
    rowspan_count = 0

    for gender in ['Men', 'Women']:
        for performance in parser.css_first(f"h3[id={gender}]").parent.next.next.css('table tbody tr'):
            tds = performance.css('td')
            
            if len(tds) < 10: continue
            
            if not rowspan_bool:
                rowspan_count = int(tds[0].attributes.get("rowspan", 0))
                
                # Discipline
                discipline = format_long_str(tds[0].text(separator=" "))
                discipline = re.sub(r'\s+', ' ', discipline)
            
            if "background" not in tds[1].attributes.get("style", '') and not tds[1].parent.attributes.get("bgcolor", False):
                
                # Time
                time = format_str(tds[1-rowspan_bool].text())
                
                # Player
                players = tds[6-rowspan_bool].css('a')
                player = format_str(players[0].text()) + (" ..." if len(players) > 1 else '')
                
                # Country
                # print(player)
                country = tds[7-rowspan_bool].css_first("a").attrs["title"]
                
                # Date
                date = format_str(tds[8-rowspan_bool].text())
                for _format in ["%d %b %Y", "%d %B %Y"]:
                    try:
                        date = datetime.strptime(date, _format).strftime("%d %b %Y")
                        break
                    except ValueError:
                        continue
                
                data += f'{discipline},{time},{player},{country},{date}\n'
            
            if rowspan_count:
                rowspan_count -= 1
            rowspan_bool = bool(rowspan_count)
        
        data += '--\n'
        
    return data
    
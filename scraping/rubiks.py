import re
import requests
from datetime import datetime

from classes.UrlManager import url_request

regex = re.compile(r'(\d{4})\s\((\d+)(?:\s?[-–]\s?\d+)?\s(\w+)\)?', re.I)
    
def extract_rubiks_wr(**kwargs) -> str:
    context = kwargs['context']
    session: requests.Session = kwargs['session']
    session.headers.update(context['headers'])
    
    _json = url_request(session, context['url'], json=True)
    session.headers.update(requests.sessions.default_headers())
    data = []
    
    for row in _json["rows"]:
        if row["event_name"] in["3x3x3 Fewest Moves",  "3x3x3 Multi-Blind"]: continue
        
        discipline = f'{row["type"].title()} {row["event_name"]}'
        
        time = row["best"] if row["type"] == "single" else row["average"]
        time = f'''{f"{time//6000}:" if time>6000 else ''}{time//100%60:02d}.{time%100:02d}'''.lstrip('0')
        if time.startswith("."):
            time = "0" + time
            
        athlete = row["person_name"]
        country = row["country_name"]
        date = datetime.strptime(row["start_date"], "%Y-%m-%d").strftime("%d %b %Y")
        
        data.append(f'{discipline},{time},{athlete},{country},{date}')
    
    data = data[::2] + ['--'] + data[1::2]
    
    return '\n'.join(data)

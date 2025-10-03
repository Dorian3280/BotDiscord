from requests import Session
from datetime import datetime
from selectolax.parser import HTMLParser
from classes.UrlManager import url_request

from classes.StringProcessor import format_long_str, format_str


def extract_swimming_wr(**kwargs) -> str:
    
    session: Session = kwargs['session']
    context: list = kwargs['context']
    url = context['url']

    data = ''
    
    for _length in context["length"]:
        for _gender in context["gender"]:
            
            _data = url_request(session, url.format(gender=_gender, length=_length), json=True)
            
            for record in _data["records"]:
                discipline = f'({context["meanings"][_length]}) {record["eventDisciplineName"]}'
                
                time = record["timeFormatted"]
                athlete = record["fullName"].title()
                country = record["nationalityName"]
                
                # Date
                date = datetime.fromisoformat(record["recordUpdated"][:-1]).strftime("%d %b %Y")
                
                data += f'{discipline},{time},{athlete},{country},{date}\n'
        
            data += '--\n'
    
    return data

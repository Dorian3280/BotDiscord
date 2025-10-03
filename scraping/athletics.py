from requests import Session
from datetime import datetime
from selectolax.parser import HTMLParser

from classes.UrlManager import url_request


def extract_athletics_wr(**kwargs) -> str:
    
    session: Session = kwargs["session"]
    url: list = kwargs["context"]["url"]
    
    parser: HTMLParser = url_request(session, url)
    
    data = ''
    
    for table in parser.css('table'):
        for row in table.css("tbody tr")[1:]:
            discipline = row.css_first("td:nth-child(1)").text()
            athlete = row.css_first("td:nth-child(2)").text(deep=False).strip()
            time = row.css_first("td:nth-child(3)").text().replace(".", ":").replace(",", ".")
            
            # Country
            try:
                country = row.css_first("td:nth-child(2) span").attributes["title"]
            except AttributeError:
                country = "-"
            
            # Date
            date = row.css_first("td:nth-child(4)").text()
            try:
                date = date[date.index("-")+1:]
            except ValueError:
                pass
            date = datetime.strptime(date, "%d.%m.%Y").strftime("%d %b %Y")
            
            data += f'{discipline},{time},{athlete},{country},{date}\n'
        
        data += '--\n'
        
    return data
    
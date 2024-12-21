import os
from datetime import datetime
from requests import Session
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str
from classes.UrlManager import url_request


def extract_speedrun_wr(**kwargs) -> str:
    
    session: Session = kwargs['session']
    context: dict = kwargs['context']
    base_url = kwargs['base_url']
    
    data = ''
    
    for game in context:
        parser: HTMLParser = url_request(session, base_url + context[game]['leaderboard'])
        
        tds = parser.css('table tbody tr:first-child td')
        player = format_str(tds[1].text())
        try:
            country = format_str(tds[1].css_first('img').attrs["alt"].split(',')[-1])
        except:
            country = '-'
        time = format_str(tds[3].text())
        
        # Date
        json = url_request(session, base_url + context[game]['history_api'], json=True)
        date = datetime.fromtimestamp(json["runList"][-1]["date"]).strftime("%d %B %Y")
    
        data += f'{game},{time},{player},{country},{date}\n'
        
    return data

import os
from requests import Session
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_long_str, format_str


def extract_speedrun_wr(parser: HTMLParser, **kwargs) -> str:
    
    tds = parser.css('table tbody tr:first-child td')
    player = format_str(tds[1].text())
    try:
        country = format_str(tds[1].css_first('img').attrs["alt"].split(',')[-1])
    except:
        country = '-'
    time = format_str(tds[3].text())
    
    return f'{kwargs['key']},{time},{player},{country}\n'

import sys
from requests import Session
from selectolax.parser import HTMLParser

from classes.DataManager import DATA


session = Session()

C = sys.argv[1]
URL = DATA[C]["url"]
SCRIPT = DATA[C]["script"]


parser = HTMLParser(session.get(URL).text)
if 'context' in DATA[C].keys():
    d = SCRIPT(parser=parser, session=session, context=DATA[C]['context'], base_url=DATA[C]['url'])
else:
    d = SCRIPT(parser=parser, session=session)

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(d)

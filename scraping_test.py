import sys
import webbrowser
from requests import Session
from selectolax.parser import HTMLParser

from classes.DataManager import DATA


session = Session()
MODE = sys.argv[1]
CAT = sys.argv[2]

URL = DATA[CAT]["url"]
SCRIPT = DATA[CAT]["script"]

if MODE == "script":

    parser = HTMLParser(session.get(URL).text)
    if 'context' in DATA[CAT].keys():
        d = SCRIPT(parser=parser, session=session, context=DATA[CAT]['context'], base_url=DATA[CAT]['url'])
    else:
        d = SCRIPT(parser=parser, session=session)

    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(d)

elif MODE == "url":
    webbrowser.open(URL)

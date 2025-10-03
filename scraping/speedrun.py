from datetime import datetime
from requests import Session
from selectolax.parser import HTMLParser

from classes.StringProcessor import format_str
from classes.UrlManager import url_request


def extract_speedrun_wr(**kwargs) -> str:
    
    session: Session = kwargs['session']
    context: list = kwargs['context']
    url = context['url']
    data = ''
    
    for game in context["games"]:
        print(game["game"])
        _data = url_request(session, url.format(game["id"]), json=True)["data"]
        
        for category in game["categories"]:
            ind = next((i for i, g in enumerate(_data) if g["category"] == category["id"]), -1)
            time = _data[ind]["runs"][0]["run"]["times"]["primary"][2:].lower()
            athlete_data = url_request(session, _data[ind]["runs"][0]["run"]["players"][0]["uri"], json=True)
            athlete = athlete_data["data"]["names"]["international"]
            try:
                country = athlete_data["data"]["location"]["country"]["names"]["international"]
            except TypeError:
                country = "-"
            date = datetime.strptime(_data[ind]["runs"][0]["run"]["date"], "%Y-%m-%d").strftime("%d %b %Y")
            
            data += f'{game["game"]} {category["name"]},{time},{athlete},{country},{date}\n'
        
    return data

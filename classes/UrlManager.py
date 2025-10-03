from requests import Session
from selectolax.parser import HTMLParser

def url_request(session: Session, url: str, json=False):
    print(f'... Requesting -> {url}')
    response = session.get(url)
    if response.status_code != 200:
        raise Exception("403")
    
    if json:
        return response.json()
    
    return HTMLParser(response.text)

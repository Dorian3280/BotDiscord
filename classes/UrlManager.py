from requests import Session
from selectolax.parser import HTMLParser

def url_request(session: Session, url: str):
    print(f'... Requesting')
    response = session.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}, status code: {response.status_code}")
        return None
    
    return HTMLParser(response.text)

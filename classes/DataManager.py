from scraping.athletics import extract_athletics_wr
from scraping.rubiks import extract_rubiks_wr
from scraping.swimming import extract_swimming_wr
from scraping.speedrun import extract_speedrun_wr


DATA = {
    'athletics': {
                "script": extract_athletics_wr,
                "header": "***Men,Women\ndiscipline,time,player,country,date",
                "context": {
                    "url": "https://etusuora.com/en/athletics/world-records",
                }
    },
    'rubiks': {
                "script": extract_rubiks_wr,
                "header": "***Single,Average\ndiscipline,time,player,country,date",
                "context": {
                    "url": "https://www.worldcubeassociation.org/results/records?show=mixed",
                    "headers": {
                        "Accept": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0 Safari/537.36",
                        "Referer": "https://www.worldcubeassociation.org/results/records?show=mixed",
                        "Cookie": "sessionid=_ga=GA1.1.2080631853.1759358121; _WcaOnRails_session=ZMWiialo2UEmJgBr16E9y7L4pY1rko5v%2F1SVDd45iPFHEME5FrXpO2FbhPGY6CZlUnf8y7vUnVcIZdL4oVKE9QRjCikvRQsqNU2fjEQDl%2BFhWs%2FbCP14N5oNcrAT3KmC1ICf1sU7r41nMiX1oVDmQAIsE0N5fvIkIvVXDmN5LcoyBMBsuB5YjyoR5bi0FAdTMwHdigswoI9XgqkJNmkukLM7zQHXlqcEqpxAxLwHwfSO8OzTNGZAa%2FfXrW7fLukzIJ3gnHPvTavo7XCC2kPmiReiByN40zvak87L%2F9nkw%2FSQ329u9P9hcP%2B12eMKTs235g2yOtCq9b55WtRnLxi8xExQrROG25%2FDhA8AeDuTKDBNe71D9138VfoBdIaZgw45%2F%2Bw1Y4AR0A%2FWH9s%3D--LDxfFbPkiQaq9tGi--w7EAmisvSFe2eMyZRXGi4w%3D%3D; _ga_QB1H9R123K=GS2.1.s1759471660$o5$g1$t1759473002$j60$l0$h0; csrftoken=DT5jvTzJUAHN00BMuEGmcRooByrh4gWHVnAD9c5_ap0C_O5UpO9w2vme4b7feiY1qrPj-vAaMRqqRcfbfyEwfg; autre=valeur",  # colle la valeur exacte depuis ton navigateur
                    }
                }
    },
    'swimming': {
                "script": extract_swimming_wr,
                "header": "***Long track 50m (Men),Long track 50m (Women),Short track 25m (Men),Short track 25m (Women)\ndiscipline,time,player,country,date",
                "context" : {
                    "url": "https://api.worldaquatics.com/fina/records/SW?recordCode=WR&gender={gender}&pool={length}",
                    "gender": ["M", "F"],
                    "length": ["LCM", "SCM"],
                    "meanings": {
                        "M": "Men",
                        "F": "Women",
                        "LCM": "50m pool",
                        "SCM": "25m pool",
                    }
                }
    },
    'speedrun': {
        "script": extract_speedrun_wr,
        "header": "***Game\ngame,player,country,time,date",
        "context": {
                    "url": "https://www.speedrun.com/api/v1/games/{}/records?top=1&scope=full-game",
                    "games": 
                        [
                            {
                                "game": "GeoGuessr",
                                "id": "m1mnj2jd",
                                "categories": [
                                { "name": "25K", "id": "n2ynny7k" },
                                { "name": "100K", "id": "7kjlejz2" }
                                ]
                            },
                            {
                                "game": "Chained Together",
                                "id": "46wrw771",
                                "categories": [
                                { "name": "Any%", "id": "q2563nyk" }
                                ]
                            },
                            {
                                "game": "Dark Souls 3",
                                "id": "k6qg0xdg",
                                "categories": [
                                { "name": "Any%", "id": "n2y143z2" },
                                { "name": "All Bosses", "id": "7kjz1ond" }
                                ]
                            },
                            {
                                "game": "Super Mario Bros",
                                "id": "om1m3625",
                                "categories": [
                                { "name": "Any%", "id": "w20p0zkn" }
                                ]
                            },
                            {
                                "game": "Celeste",
                                "id": "o1y9j9v6",
                                "categories": [
                                { "name": "Any%", "id": "7kjpl1gk" }
                                ]
                            },
                            {
                                "game": "Portal",
                                "id": "4pd0n31e",
                                "categories": [
                                { "name": "Out of Bounds", "id": "lvdowokp" },
                                { "name": "Inbounds", "id": "7wkp6v2r" },
                                { "name": "Inbounds no SLA", "id": "n2yq98ko" },
                                { "name": "Glitchless", "id": "wk6pexd1" }
                                ]
                            }
                        ]
                    }
                }
}

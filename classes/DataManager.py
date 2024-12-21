from scraping.athletics import extract_athletics_wr
from scraping.rubiks import extract_rubiks_wr
from scraping.swimming import extract_swimming_wr
from scraping.speedrun import extract_speedrun_wr

DATA = {
    'athletics': {
                  "script": extract_athletics_wr,
                  "header": "***Men,Women\ndiscipline,time,player,country,date\n",
                  "url": "https://en.wikipedia.org/wiki/List_of_world_records_in_athletics",
    },
    'rubiks': {
                  "script": extract_rubiks_wr,
                  "header": "***Single,Average\ndiscipline,time,player,country\n",
                  "url": "https://en.wikipedia.org/wiki/List_of_world_records_in_speedcubing",
    },
    'swimming': {
                  "script": extract_swimming_wr,
                  "header": "***Long course 50m (Men),Short course 25m (Men),Long course 50m (Women),Short course 25m (Women)\ndiscipline,time,player,country,date\n",
                  "url": "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming",
    },
    'speedrun': {
                  "script": extract_speedrun_wr,
                  "header": "***Game\ngame,player,country,time\n",
                  "url": {
                        'Chained Together': 'https://www.speedrun.com/fr-FR/Chained_Together?h=any-nowings-1-player-restricted-v1-7-3&x=q2563nyk-9l7yyj9l.qzn4yekq-r8rrrvw8.q657gknl-jlzpp4xn.qke8609q',
                        'Dark Souls 3 Any%': 'https://www.speedrun.com/fr-FR/darksouls3?h=Any&x=n2y143z2',
                        'Dark Souls 3 All Bosses': 'https://www.speedrun.com/fr-FR/darksouls3?h=All_Bosses-Restricted&x=7kjz1ond-r8reg92l.12vved7q',
                        'Super Mario Bros': 'https://www.speedrun.com/fr-FR/smb1?h=Any-NTSC&x=w20p0zkn-onvvdymn.013zwgxq',
                        'Celeste': 'https://www.speedrun.com/fr-FR/celeste?h=Any&x=7kjpl1gk',
                        'Portal Out of Bounds': 'https://www.speedrun.com/fr-FR/portal?h=Out_of_Bounds-PC&x=lvdowokp-kn0mz7ol.jq6nxjnl',
                        'Portal Inbounds': 'https://www.speedrun.com/fr-FR/portal?h=Inbounds-PC&x=7wkp6v2r-kn0mz7ol.jq6nxjnl',
                        'Portal Inbounds no SLA': 'https://www.speedrun.com/fr-FR/portal?h=Inbounds_No_SLA-PC-Legacy&x=n2yq98ko-kn0mz7ol.jq6nxjnl-ql61qmv8.jqz97g41',
                        'Portal Glitchless': 'https://www.speedrun.com/fr-FR/portal?h=Glitchless-PC&x=wk6pexd1-kn0mz7ol.jq6nxjnl',
                    },
    },
}

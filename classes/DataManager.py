from scraping.athletics import extract_athletics_wr
from scraping.rubiks import extract_rubiks_wr
from scraping.swimming import extract_swimming_wr
from scraping.speedrun import extract_speedrun_wr


DATA = {
    'athletics': {
                  "script": extract_athletics_wr,
                  "header": "***Men,Women\ndiscipline,time,player,country,date",
                  "url": "https://en.wikipedia.org/wiki/List_of_world_records_in_athletics",
    },
    'rubiks': {
                  "script": extract_rubiks_wr,
                  "header": "***Single,Average\ndiscipline,time,player,country,date",
                  "url": "https://en.wikipedia.org/wiki/List_of_world_records_in_speedcubing",
    },
    'swimming': {
                  "script": extract_swimming_wr,
                  "header": "***Long course 50m (Men),Long course 50m (Women),Short course 25m (Men),Short course 25m (Women)\ndiscipline,time,player,country,date",
                  "url": "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming",
    },
    'speedrun': {
                  "script": extract_speedrun_wr,
                  "header": "***Game\ngame,player,country,time,date",
                  "url": "https://www.speedrun.com",
                  "context": {
                        'GeoGuessr 25K': {
                            "leaderboard": "/fr-FR/geoguessr?h=25K-acw&x=n2ynny7k-5lyx7zkn.z19ngj4q",
                            "history_api": "/api/v2/GetGameLeaderboard2?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6Im4yeW5ueTdrIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6Im0xbW5qMmpkIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjIsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiI1bHl4N3prbiIsInZhbHVlSWRzIjpbInoxOW5najRxIl19XSwidmlkZW8iOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNzUwNDU3NzcyfQ"
                        },
                        'GeoGuessr 100K': {
                            "leaderboard": "/fr-FR/geoguessr?h=100K-acw&x=7kjlejz2-5lyx7zkn.z19ngj4q",
                            "history_api": "/api/v2/GetGameLeaderboard2?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6IjdramxlanoyIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6Im0xbW5qMmpkIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjIsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiI1bHl4N3prbiIsInZhbHVlSWRzIjpbInoxOW5najRxIl19XSwidmlkZW8iOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNzUwNDU3NzcyfQ"
                        },
                        'Chained Together': {
                            "leaderboard": "/fr-FR/Chained_Together?h=any-nowings-1-player-restricted-v1-7-3&x=q2563nyk-9l7yyj9l.qzn4yekq-r8rrrvw8.q657gknl-jlzpp4xn.qke8609q",
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6InEyNTYzbnlrIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6IjQ2d3J3NzcxIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjIsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiI5bDd5eWo5bCIsInZhbHVlSWRzIjpbInF6bjR5ZWtxIl19LHsidmFyaWFibGVJZCI6InI4cnJydnc4IiwidmFsdWVJZHMiOlsicTY1N2drbmwiXX0seyJ2YXJpYWJsZUlkIjoiamx6cHA0eG4iLCJ2YWx1ZUlkcyI6WyJxa2U4NjA5cSJdfV0sInZpZGVvIjowfSwicGFnZSI6MSwidmFyeSI6MTczNDYzNTgyNX0"
                        },
                        'Dark Souls 3 Any%': {
                            "leaderboard": '/fr-FR/darksouls3?h=Any&x=n2y143z2',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6Im4yeTE0M3oyIiwiZW11bGF0b3IiOjEsImdhbWVJZCI6Ims2cWcweGRnIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjIsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOltdLCJ2aWRlbyI6MH0sInBhZ2UiOjEsInZhcnkiOjE3MzQ3NDM0NDR9"
                        },
                        'Dark Souls 3 All Bosses': {
                            "leaderboard": '/fr-FR/darksouls3?h=All_Bosses-Restricted&x=7kjz1ond-r8reg92l.12vved7q',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6Ijdranoxb25kIiwiZW11bGF0b3IiOjEsImdhbWVJZCI6Ims2cWcweGRnIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjIsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiJyOHJlZzkybCIsInZhbHVlSWRzIjpbIjEydnZlZDdxIl19XSwidmlkZW8iOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNzM0NzQzNDQ0fQ"
                        },
                        'Super Mario Bros': {
                            "leaderboard": '/fr-FR/smb1?h=Any-NTSC&x=w20p0zkn-onvvdymn.013zwgxq',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6IncyMHAwemtuIiwiZW11bGF0b3IiOjEsImdhbWVJZCI6Im9tMW0zNjI1Iiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjAsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiJvbnZ2ZHltbiIsInZhbHVlSWRzIjpbIjAxM3p3Z3hxIl19XSwidmlkZW8iOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNzM0NzUxNjU3fQ"
                        },
                        'Celeste': {
                            "leaderboard": '/fr-FR/celeste?h=Any&x=7kjpl1gk',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6IjdranBsMWdrIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6Im8xeTlqOXY2Iiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjIsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOltdLCJ2aWRlbyI6MH0sInBhZ2UiOjEsInZhcnkiOjE3MzQ3MTY1NTN9"
                        },
                        'Portal Out of Bounds': {
                            "leaderboard": '/fr-FR/portal?h=Out_of_Bounds-PC&x=lvdowokp-kn0mz7ol.jq6nxjnl',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6Imx2ZG93b2twIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6IjRwZDBuMzFlIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjAsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiJrbjBtejdvbCIsInZhbHVlSWRzIjpbImpxNm54am5sIl19XSwidmlkZW8iOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNzM0NzY4MjA1fQ"
                        },
                        'Portal Inbounds': {
                            "leaderboard": '/fr-FR/portal?h=Inbounds-PC&x=7wkp6v2r-kn0mz7ol.jq6nxjnl',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6Ijd3a3A2djJyIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6IjRwZDBuMzFlIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjAsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiJrbjBtejdvbCIsInZhbHVlSWRzIjpbImpxNm54am5sIl19XSwidmlkZW8iOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNzM0NzY4MjA1fQ"
                        },
                        'Portal Inbounds no SLA': {
                            "leaderboard": '/fr-FR/portal?h=Inbounds_No_SLA-PC-Legacy&x=n2yq98ko-kn0mz7ol.jq6nxjnl-ql61qmv8.jqz97g41',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6Im4yeXE5OGtvIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6IjRwZDBuMzFlIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjAsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiJrbjBtejdvbCIsInZhbHVlSWRzIjpbImpxNm54am5sIl19LHsidmFyaWFibGVJZCI6InFsNjFxbXY4IiwidmFsdWVJZHMiOlsianF6OTdnNDEiXX1dLCJ2aWRlbyI6MH0sInBhZ2UiOjEsInZhcnkiOjE3MzQ3NjgyMDV9"
                        },
                        'Portal Glitchless': {
                            "leaderboard": '/fr-FR/portal?h=Glitchless-PC&x=wk6pexd1-kn0mz7ol.jq6nxjnl',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6IndrNnBleGQxIiwiZW11bGF0b3IiOjAsImdhbWVJZCI6IjRwZDBuMzFlIiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjAsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiJrbjBtejdvbCIsInZhbHVlSWRzIjpbImpxNm54am5sIl19XSwidmlkZW8iOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNzM0NzY4MjA1fQ"
                        },
                        'Get To Work': {
                            "leaderboard": '/fr-FR/Get_to_Work?h=glitchless&x=5dww54gd',
                            "history_api": "/api/v2/GetGameRecordHistory?_r=eyJwYXJhbXMiOnsiY2F0ZWdvcnlJZCI6IjVkd3c1NGdkIiwiZW11bGF0b3IiOjEsImdhbWVJZCI6ImoxbjRyMHk2Iiwib2Jzb2xldGUiOjAsInBsYXRmb3JtSWRzIjpbXSwicmVnaW9uSWRzIjpbXSwidGltZXIiOjIsInZlcmlmaWVkIjoxLCJ2YWx1ZXMiOltdLCJ2aWRlbyI6MH0sInBhZ2UiOjEsInZhcnkiOjE3MzYyODk2MzZ9"
                        },
                    }
    }
}

from requests import Session
from itertools import groupby, chain

from classes.DataManager import DATA
from classes.UrlManager import url_request
from classes.FileManager import FileManager
from classes.StringProcessor import from_csv_to_table, from_csv_to_set

from medias.discord_emoji import *


class Manager:
    def __init__(self, datablase_url, config):
        self.session = Session()
        self.file_manager = FileManager(datablase_url)
        self.config = config


    def get_one(self, category: str, sorting=False):
        filename = f"{category}.{self.config['extension_db_file']}"
        
        data = self.file_manager.read(filename)
        header, body = self.format_data(data, DATA[category]['header'])

        return from_csv_to_table(body, category, header)


    def format_data(self, data: str, header: str):
        categories, header = header.split('\n')
        categories = categories[3:].split(',')
        header = header.split(',')

        body = map(lambda row: row.split(','), data.splitlines())
        body = map(list, (group for key, group in groupby(body, lambda x: "--" in x) if not key))
        body = {category: block for category, block in zip(categories, body)}
        
        return header, body
        

    def get_url(self, category: str):
        return DATA[category]['url']


    def get_all(self, categories: list[str]):
        return "\n\n".join([self.get_one(category) for category in categories])
    

    def extract_one(self, category):
        context = DATA[category]

        if 'context' in DATA[category].keys():
            data = DATA[category]['script'](session=self.session, context=DATA[category]['context'], base_url=context['url'])
        else:
            parser = url_request(self.session, context['url'])
            data = DATA[category]['script'](parser=parser, category=category, session=self.session)
        
        return data


    def extract_new_wr(self, data, filename) -> list[str]:
        old = self.file_manager.read(filename)
        
        return list(from_csv_to_set(data).difference(from_csv_to_set(old)))

    
    def launch(self, category):
        filename = f"{category}.{self.config['extension_db_file']}"
        
        print('Executing ', category + '...')
        data = self.extract_one(category)
        
        new_wr = self.extract_new_wr(data, filename)
        
        if not self.file_manager.is_exist(filename) or new_wr:
            self.file_manager.write(filename, data)
        
        return new_wr
    
    
    def check_new_wr(self, categories: list) -> str:        
        new_wr = {
            category: self.launch(category)
            for category in categories
        }
        
        # Build the loop with good format, chain just here for the flat
        return chain.from_iterable([self.format_new_wr(v, key) for v in values] for key, values in new_wr.items() if values is not None)
        
    
    def format_new_wr(self, row: str, category: str):
        discipline, time, player_name, country, date = row.strip().split(',')
        return f"## :trophy: __**New {category.title()} World Record**__ :trophy: \n# **:{category_emoji[category]}: {discipline}**\n:timer:  {time}\n:calendar: {date}\n:first_place: {player_name} :{emoji_flags[country]}:"

from requests import Session
from itertools import groupby, chain

from classes.DataManager import DATA
from classes.UrlManager import url_request
from classes.FileManager import FileManager
from classes.StringProcessor import from_csv_to_table, from_csv_to_set

from medias.discord_emoji import *


class Manager:
    def __init__(self, datablase_url, bot):
        self.session = Session()
        self.file_manager = FileManager(datablase_url)
        self.bot = bot


    def get_one(self, category: str):
        filename = f"{category}.{self.bot.config['extension_db_file']}"
        
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


    def extract_new_wr(self, old: list[str], new: list[str]) -> list[str]:
        time_new = [row.split(',')[1] for row in new if len(row) > 5]
        time_old = [row.split(',')[1] for row in old if len(row) > 5]
        ind = [i for i, (a, b) in enumerate(zip(time_new, time_old)) if a != b]
        
        return [new[i] for i in ind]

    
    def launch(self, category):
        filename = f"{category}.{self.bot.config['extension_db_file']}"
        
        print(f'\nExtracting {category.title()}')
        new = DATA[category]['script'](session=self.session, category=category, context=DATA[category]["context"])
        old = self.file_manager.read(filename)
        
        # Comparing
        new_formatted = [row for row in new.split('\n') if len(row) > 5]
        old_formatted = [row for row in old.split('\n') if len(row) > 5]
        new_wr = self.extract_new_wr(old_formatted, new_formatted)
    
        if not self.file_manager.is_exist(filename) or new_wr:
            self.file_manager.write(filename, new)
        
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
        
        if country not in emoji_flags:
            self.bot.logger.error(f"Country not found in flag media: {country}")
            
        flag = f" :{emoji_flags[country]}:" if country in emoji_flags else ""
        
        return (
            f"## :trophy: __**{category.title()} New World Record**__ :trophy: \n"
            f"# **{category_emoji[category]} {discipline}**\n"
            f":first_place: {player_name}{flag}\n"
            f":timer:  {time}\n"
            f":calendar: {date}\n"
        )

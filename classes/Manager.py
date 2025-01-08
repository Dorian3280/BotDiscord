from requests import Session
from itertools import groupby

from classes.DataManager import DATA
from classes.UrlManager import url_request
from classes.FileManager import FileManager
from classes.StringProcessor import from_csv_to_table

from medias.emoji_flags import emoji_flags


class Manager:
    def __init__(self, datablase_url, config):
        self.session = Session()
        self.file_manager = FileManager(datablase_url)
        self.config = config


    def get_one(self, category: str, sorting=False):
        filename = f"{category}.{self.config['extension_db_file']}"
        
        data = self.file_manager.read(filename)
        header, body = self.format_data(data, DATA[category]['header'])
        
        if sorting:
            body = self.sorting_by(body)

        return from_csv_to_table(body, category, header)


    def format_data(self, data: str, header: str):
        categories, header = header.split('\n')
        categories = categories[3:].split(',')
        header = header.split(',')

        body = map(lambda row: row.split(','), data.splitlines())
        body = map(list, (group for key, group in groupby(body, lambda x: "--" in x) if not key))
        body = {category: block for category, block in zip(categories, body)}
        
        return header, body


    def sorting_by(data, sorting):
        match sorting:
            case 'name':
                ...
        

    def get_url(self, category: str):
        return DATA[category]['url']


    def get_all(self, categories: list[str]):
        return "\n\n".join([self.get_one(category) for category in categories])
    

    def execute_one(self, category):
        context = DATA[category]
        print(category + ' ->\n... Executing')
        filename = f"{category}.{self.config['extension_db_file']}"

        if 'context' in DATA[category].keys():
            data = DATA[category]['script'](session=self.session, context=DATA[category]['context'], base_url=context['url'])
        else:
            parser = url_request(self.session, context['url'])
            data = DATA[category]['script'](parser=parser, category=category, session=self.session)
        
        if not self.file_manager.is_exist(filename):
            self.file_manager.write(filename, data)
            return None

        diff = self.file_manager.test_if_equal(data, filename)
        
        if diff is None:
            return None

        # write
        self.file_manager.write(filename, data)

        return diff
    
    
    def format_new_wr(self, row: str):
        print(row)
        discipline, time, player_name, country, *_ = row.strip().split(',')
        return f"❗ 🎉   __**[{discipline}] {time}  ⏲️ NEW WR**__    🎉 ❗\n 🏆 {emoji_flags[country]}   {player_name} 🏆"

from requests import Session

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


    def get_one(self, category: str):
        filename = f"{category}.{self.config['extension_db_file']}"
        data = self.file_manager.read(filename)

        return from_csv_to_table(data, category, DATA[category]['header'])


    def get_url(self, category: str):
        return DATA[category]['url']


    def get_all(self, categories: list[str]):
        return "\n\n".join([self.get_one(category) for category in categories])
    

    def execute_one(self, category):
        context = DATA[category]
        print(category + ' ->\n... Executing')
        filename = f"{category}.{self.config['extension_db_file']}"

        if isinstance(context['url'], str):
            parser = url_request(self.session, context['url'])
            if parser is not None:
                data = DATA[category]['script'](parser, category=category, session=self.session)

        elif isinstance(context['url'], dict):
            data = ""
            for k, url in context['url'].items():
                parser = url_request(self.session, url)
                if parser is not None:
                    data += DATA[category]['script'](parser, key=k, session=self.session)

        elif isinstance(context['url'], list):
            pass

        else:
            pass

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
        discipline, time, player_name, country, *_ = row.strip().split(',')
        return f"❗ 🎉   __**[{discipline}] {time}  ⏲️ NEW WR**__    🎉 ❗\n 🏆 {emoji_flags[country]}   {player_name} 🏆"

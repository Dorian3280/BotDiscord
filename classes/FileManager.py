import os

class FileManager:
    def __init__(self, url: str):
        self.url = url

    def read(self, path):
        path = os.path.join(self.url, path)
        if not self.is_exist(path): return None
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


    def write(self, path: str, text: str):
        path = os.path.join(self.url, path)
        dir_path = os.path.dirname(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(path, 'w', encoding="utf-8") as f:
            print("... Writing")
            f.write(text)

    def is_exist(self, path: str):
        return os.path.isfile(os.path.join(self.url, path))
    
    def test_if_equal(self, data, filename):
        old = self.read(filename)

        if data == old:
            return None

        return list(set(data).difference(set(old)))

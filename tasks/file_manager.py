import os


class FileOperator:
    def __init__(self, path):
        self.path = path
        self.content = self.get_content()

    @property
    def fullpath(self):
        return os.path.abspath(self.path)

    def get_content(self):
        with open(self.fullpath) as f:
            content = f.read()
        return content

    def save(self, text):
        with open(self.fullpath, 'w') as f:
            f.write(text)

class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content
    def __str__(self):
        return self.name + ';' + self.content.replace('\n', '\\n')

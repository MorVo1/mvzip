class File:
    def __init__(self, name):
        self.name = name
        self.content = self.get_content(self.name)
    

    def get_content(self, name):
        return open(name).read() 


    def __str__(self):
        return self.name + ';' + self.content.replace('\n', '\\n')

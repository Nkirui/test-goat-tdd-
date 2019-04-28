class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
      
    def json(self):
        data = { 
            "Title": self.title,
            "Content": self.content,
            # "Date":datetime.date
        }
        return data
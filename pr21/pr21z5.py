class Book:
    __slots__ = ('title', 'author')
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def info(self):
        print(f" '{self.title}' — автор: {self.author}")

book = Book("1984", "Дж. Оруэлл")
book.info()

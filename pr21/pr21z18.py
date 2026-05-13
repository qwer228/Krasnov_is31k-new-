class Message:
    __slots__ = ('text', 'author')
    
    def __init__(self, text, author):
        self.text = text
        self.author = author
    
    def format(self):
        return f"{self.author}: {self.text}"

msg = Message("Привет!", "Алексей")
print(msg.format())

class SafeFileManager:
    def __init__(self, filename, mode, encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            return self.file
        except Exception as e:
            print(f"Ошибка открытия файла: {e}")
            return None
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("File closed")
        return True  # Подавляем исключения

# Использование
with SafeFileManager('input.txt', 'r') as file:
    if file:
        try:
            content = file.read()
            print(content)
        except Exception as e:
            print(f"Ошибка чтения: {e}")

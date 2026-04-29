from datetime import datetime

with open('log.txt', 'a', encoding='utf-8') as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Сообщение лога\n")

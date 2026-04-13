from datetime import datetime

# Решение
message = "Script executed successfully"

with open('messages.log', 'a', encoding='utf-8') as f:
    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f"[{timestamp_str}] {message}\n")

print("Сообщение записано.")

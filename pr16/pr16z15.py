import re
text = "hello world from python"
print(re.sub(r'\b\w', lambda m: m.group(0).upper(), text))
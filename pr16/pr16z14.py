import re
text = "hello  hello  world"
print(re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE))
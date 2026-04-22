import re
text = "Visit https://google.com and http://example.org for info"
print(re.findall(r'https?://[^\s<>]+', text))
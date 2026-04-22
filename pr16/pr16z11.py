import re
text = "I am a boy and you"
print(re.sub(r'\b\w{1,2}\b', '***', text))
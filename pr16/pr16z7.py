import re
text = "+37112345678"
print(bool(re.match(r'^\+371\d{8}$', text)))
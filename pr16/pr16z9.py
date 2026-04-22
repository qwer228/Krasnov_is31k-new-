import re
password = "SecurePass1"
print(bool(re.match(r'^(?=.*\d).{8,}$', password)))
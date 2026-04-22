import re
card = "1234 5678 9012 3456"
digits = re.sub(r'\s', '', card)
masked = '*' * (len(digits) - 4) + digits[-4:]
print(' '.join([masked[i:i+4] for i in range(0, len(masked), 4)]))
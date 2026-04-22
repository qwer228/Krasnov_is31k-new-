import re
text = " Name :  John   Age : 25"
name = re.search(r'Name\s*:\s*([A-Za-z]+)', text)
age = re.search(r'Age\s*:\s*(\d+)', text)
print({'name': name.group(1), 'age': int(age.group(1))})
# Regular Expression (RegEx)
# Metacharacters... Special Characters => $ . + [] () ^

# import re 

# text = "Hello, My name is John Wick."
# pattern = r"Roy"
# match = re.search(pattern, text)
# if match:
#     print("Name found")
# else:
#     print("Not found")

# (xxx) xxx-xxxx
import re
'''
pattern = r"\(\d{3}\) \d{3}-\d{4}"
phone_number = "(123) 4556-789"

match = re.match(pattern, phone_number)
if match:
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")
'''

text = "This  is   a   sentence    with    multiple    spaces."
pattern = r"\s+"

res = re.sub(pattern, "", text.title())
print(text)
print(res)
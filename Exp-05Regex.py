
import re

text = input("Enter the text: ")

email = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

print("Extracted Email:")
for e in email:
    print(e)


noun = input("Enter a singular noun: ")

if noun.endswith("y") and noun[-2].lower() not in "aeiou":
    plural = noun[:-1] + "ies"
elif noun.endswith(("s", "sh", "ch", "x", "z")):
    plural = noun + "es"
else:
    plural = noun + "s"

print("Singular:", noun)
print("Plural:", plural)

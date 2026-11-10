
plural = input("Enter a plural noun: ")

if plural.endswith("ies"):
    singular = plural[:-3] + "y"
elif plural.endswith(("ches", "shes", "xes", "zes", "sses")):
    singular = plural[:-2]
elif plural.endswith("s"):
    singular = plural[:-1]
else:
    singular = plural

print("Singular:", singular)

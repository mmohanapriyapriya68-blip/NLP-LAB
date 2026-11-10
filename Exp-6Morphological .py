
root = input("Enter the root word: ")

suffixes = ["", "s", "ed", "ing", "er", "ly"]
prefixes = ["re", "un"]

print("Generated word forms:")

for suffix in suffixes:
    print(root + suffix)

for prefix in prefixes:
    print(prefix + root)

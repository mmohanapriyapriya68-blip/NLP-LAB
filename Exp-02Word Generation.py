
root_word = input("Enter the root word: ")

prefixes = ["un", "re", "dis", "pre", "mis"]
suffixes = ["ly", "ed", "er", "y", "ness"]

print("\nGenerated words using prefixes:")
for prefix in prefixes:
    print(prefix + root_word, end=" ")

print("\n\nGenerated words using suffixes:")
for suffix in suffixes:
    print(root_word + suffix, end=" ")

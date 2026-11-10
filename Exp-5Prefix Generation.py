
word = input("Enter word: ")

prefixes = ["un", "re", "dis", "pre", "mis", "over", "under"]

print("Generated words:")
for prefix in prefixes:
    print(prefix + word)

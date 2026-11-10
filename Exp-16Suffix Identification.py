
word = input("Enter a word: ")

prefixes = ["un", "re", "dis", "pre", "mis", "over", "under"]
suffixes = ["ing", "ed", "ly", "ness", "ful", "less", "er", "s"]

prefix = "None"
suffix = "None"

for p in prefixes:
    if word.startswith(p):
        prefix = p
        break

for s in suffixes:
    if word.endswith(s):
        suffix = s
        break

print("Word:", word)
print("Prefix:", prefix)
print("Suffix:", suffix)

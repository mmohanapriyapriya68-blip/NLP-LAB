
num = int(input("Enter a number: "))

if 10 <= num % 100 <= 20:
    suffix = "th"
else:
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")

print("Ordinal:", str(num) + suffix)

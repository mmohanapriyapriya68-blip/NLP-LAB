
num = int(input("Enter a number: "))

ones = ["", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]

def number_to_words(n):
    if n == 0:
        return "zero"

    if n < 10:
        return ones[n]

    elif n < 20:
        return teens[n - 10]

    elif n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 else "")

    elif n < 1000:
        remainder = n % 100
        result = ones[n // 100] + " hundred"
        if remainder:
            result += " and " + number_to_words(remainder)
        return result

    else:
        return "Number out of range"

print(number_to_words(num))

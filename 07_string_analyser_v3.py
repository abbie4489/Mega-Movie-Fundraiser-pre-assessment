"""In this version i use Python's RE tool to help analyse the given string,
work out whether or not it contains numbers, and then separate the string into
amount and item"""
import re

test_strings = [
    "Popcorn",  # String with no number
    "2 pc",  # String with a space than valid number
    "1.5Oj",  # String with a preceding decimal
    "4OJ",  # string with a preceding integer but no space
    ]

for item in test_strings:
    # Regular expression to test and find out id an item starts with a number
    number_regex = "^[1-9]"

    # if item has a number, separate the item into two: number and item
    if re.match(number_regex, item):
        amount = int(item[0])
        snack = item[1:]

    # If item has no number, assume number required is 1
    else:
        amount = 1
        snack = item

    # Need to remove white space from around snack
    snack = snack.strip()

    # print order
    print(f"Snack: {snack}")
    print(f"Length of Snack: {len(snack)}")
    print(f"Amount: {amount}")




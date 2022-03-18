""" 3rd iteration if the interger checking function
Simplified try/except and created AGE_RANGE as a constant
"""


def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter and integer (ie a whole number"
                  " with not decimals)")


# Main Routine
# Check for a valid age - must be between 12 and 110
AGE_RANGE = range(12, 111)  # between 12 and 110 inclusive
age = number_checker("Please enter the age of the ticket-holder: ")
while age not in AGE_RANGE:
    age = number_checker("\n please enter an integer between 12 and 110: ")

print(f"Age = {age}")

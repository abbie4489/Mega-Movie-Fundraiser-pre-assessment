""" 4rd iteration of the integer checking function
Wanted to limit the possibility of getting a false age for children < 12
this meant creating upper and lower age limits as constants
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
# Check for a valid age
MINIMUM_AGE = 12
MAXIMUM_AGE = 110
age = number_checker("Please enter the age of the ticket-holder: ")
if age < MINIMUM_AGE:  # age must be between 12 and 110
    print("Sorry, you are too young for this movie")
else:
    while age <= MAXIMUM_AGE:  # age must be between 12 and 110
        age = number_checker("\n please enter an integer between 12 and 110: ")

print(f"Age = {age}")

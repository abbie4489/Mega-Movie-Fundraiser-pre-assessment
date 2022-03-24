"""Adding 01_name_not_blank_v3 to original v1 of this base code
"""

# Import statements

# Functions go here

# Check that the ticket name is not blank


def not_blank(question):
    while True:
        response = input(question)
        if not response:
            print("You can't leave this blank...")
        else:
            return response


# Check for valid integer (eg for age)
def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter and integer (ie a whole number"
                  " with not decimals)")

# main routine

# set up dictionaries / list needed to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# loop to get ticket details
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count < MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left")
    else:
        #  warns user there is only one seat left
        print(f"\n**** You have ONLY one seat left! ****")
    #  get details
    name = not_blank("Whats your name? ")
    if name == "Xxx":
        break
    else:
        MINIMUM_AGE = 12
        MAXIMUM_AGE = 110
        age = number_checker("Please enter the age if the ticket-holder: ")
        if age < MINIMUM_AGE:  # age must be between 12 and 110
            print("Sorry, you are too young for this movie")
        else:
            while not age <= MAXIMUM_AGE:
                age = number_checker(f"\nAt {age} {name} is very old."
                                     f" please re-enter {name}'s age: ")
            count += 1  # Don't want to include escape code in the count

if count < MAX_TICKETS:
    print(f"\nYou have sold {count}  tickets\nThere are still "
          f"{MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")

    # Get age (between 12 and 130)

    # calculate snack prices

    # Ask for payment method (an apply surcharge if necessary)

# calculate total sales and profit

# output data to text file

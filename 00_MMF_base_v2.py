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


# main routine

# set up dictionaries / list needed to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# loop to get ticket details

    # get name (cant be blank)
    name = not_blank("Whats your name: ")

    # Get age (between 12 and 130)

    # calculate snack prices

    # Ask for payment method (an apply surcharge if necessary)

# calculate total sales and profit

# output data to text file

"""Adding 01_name_not_blank_v3 to original v1 of this base code
"""

# Import statements

# Functions go here

# Calculate the ticket price based on the given age
def calculate_ticket_price(age):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        price = child_price
    elif age in standard_age:
        price = standard_price
    else:
        price = retired_price
    return(price)

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
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00

name = ""
ticket_count = 0
profit = 0

while name != "Xxx" and ticket_count < MAX_TICKETS:
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nYou have {MAX_TICKETS - ticket_count} seats left")
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
            ticket_count += 1  # Don't want to include escape code in the ticket_count

            # Calculate ticket price
            ticket_price = calculate_ticket_price(age)
            print(F"For {name} the price is ${ticket_price:,.2f}")
            profit += (ticket_price - TICKET_COST_PRICE)

if ticket_count < MAX_TICKETS:
    print(f"\nYou have sold {ticket_count}  tickets\nThere are still "
          f"{MAX_TICKETS - ticket_count} available")
else:
    print("\nYou have sold all the available tickets")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # calculate snack prices

    # Ask for payment method (an apply surcharge if necessary)

# calculate total sales and profit

# output data to text file

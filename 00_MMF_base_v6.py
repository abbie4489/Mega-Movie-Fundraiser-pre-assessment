"""Adding 04_calculate_ticket_price_v4
Also include total profit calculation in main routine.
have changed the variable 'count' to 'ticket_count' and made the formatting
and language in the print statements easier to understand.
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
    return price

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

while name != "xxx" and ticket_count < MAX_TICKETS:
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nThere are {MAX_TICKETS - ticket_count} tickets left")
    else:
        #  warns user there is only one ticket left
        print(f"\n**** There is ONLY one ticket left! ****")
    #  get details
    name = not_blank("Enter ticket-holders name: ")
    if name == "xxx":
        break
    else:
        MINIMUM_AGE = 12
        MAXIMUM_AGE = 110
        age = number_checker(f"Please enter {name}'s age: ")
        if age < MINIMUM_AGE:  # age must be between 12 and 110
            print("Sorry, you are too young for this movie")
        else:
            while not age <= MAXIMUM_AGE:
                age = number_checker(f"\nAt {age} {name} is very old."
                                     f" please re-enter {name}'s age: ")
            ticket_count += 1  # Don't want to include escape code in the ticket_count

            # Calculate ticket price
            ticket_price = calculate_ticket_price(age)
            print(f"For {name} the price is ${ticket_price:,.2f}")
            profit += (ticket_price - TICKET_COST_PRICE)

# calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:  # Making sure it reads OK when only one ticket sold
        print(f"\n{ticket_count} tickets have now been sold")
    else:
        print(f"1 ticket has now been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        print("1 ticket is still available\n")  # Making sure is reads ok when
else:
    print("\nYou have sold all the available tickets")
    print("*" * 60)
print(f"Ticket profit is ${profit:.2f}")
# Get age (between  12 and 130)

# Calculate ticket price

# calculate snack prices

# Ask for payment method (an apply surcharge if necessary)


# output data to text file

"""“Moved the check of sales against maximum tickets into its own function
Added lists to hold ticket holder's name and the price paid for their ticket
Added a dictionary to get data from these 2 new lists
Added code to append name and ticket price to the new lists (line 137 and 138)
Added the import re and import pandas libraries (installing pandas package if
necessary)
I Added the print statement for ticket profit on line 151
Modified the 'else' statements under if MAX_TICKETS - ticket_count > 1:'
(previously occupied lines 158-160) to improve flow and readability
Added the print details (movie_frame: bottom 3 lines) which uses the pandas
library to create a printable DataFrame based on the dictionary
"""

# Import statements
import pandas
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


def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"\nThere are {maximum - sold} tickets left")
    else:
        # Warns user there is only one seat left
        print(f"\n**** There is ONLY ONE ticket left! ****")


def check_valid_age(minimum, maximum):
    age = number_checker(f"Please enter {name}'s age: ")
    if age < minimum:
        print(f"Sorry, {name} is too young for this movie")
        return None
    else:
        while not age <= maximum: # age must be between 12 and 110
            age = number_checker(f"\nAt {age} {name} is very old."
                                 f" Please re-enter {name}'s age: ")
        return age
# main routine

# set up dictionaries / list needed to hold data
all_names = []
all_tickets = []

# Data Frame Dictionaries / lists needed to hold data
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

MINIMUM_AGE = 12
MAXIMUM_AGE = 110
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0


# Ask user if they have used the program before and
# show instructions if necessary

# loop to get ticket details
# Initialise loop so that is runs at least once

while name != "xxx" and ticket_count < MAX_TICKETS:
    # Check to ensure there are still tickets left
    check_max_tickets(MAX_TICKETS, ticket_count)

    # Get details
    # Get name
    name = not_blank("Enter ticket-holders name: ")  # name can't be blank
    if name == "xxx":
        break
    else:
        # Check for a valid age and then calculate ticket price
        age = check_valid_age(MINIMUM_AGE, MAXIMUM_AGE)
        if not age:
            continue  # restarts the get tickets loop
        else:
            ticket_count += 1  # Don't want to include escape code in the ticket_count

        # Calculate ticket price
        ticket_price = calculate_ticket_price(age)
        print(f"For {name} the price is ${ticket_price:,.2f}")
        profit += (ticket_price - TICKET_COST_PRICE)

        # Add name and ticket price to lists
        all_names.append(name)
        all_tickets.append(ticket_price)

        # get snacks

        # get payment method (and work out surcharge as necessary)

    # end of tickets/snacks/payment loop

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
        # only one ticket is left

else:
    print("\n!!!!!!!!All available tickets have now been sold!!!!!!!!")
    print("*" * 60)

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)
print(f"Ticket profit is ${profit:.2f}")

# Loop to ask for snacks

# output data to text file

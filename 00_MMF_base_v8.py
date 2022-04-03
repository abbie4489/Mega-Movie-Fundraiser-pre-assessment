"""Added 06_String_Validator_v6 to 00_MMF_base_v7

"""

# Import statements
import re
import pandas


# Functions go here
# This function splits snacks into quantity and snack name
# It has to be called before the snack (name) can be evaluated against the
# valid_snacks list
def split_order(choice):
    # Regular expression to test and find out if an item starts with a number
    number_regex = "^[1-9]"

    # if a item has a number, separate the item into two: number and item
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]

    # if item has no number, assume number required is 1
    else:
        quantity_required = 1
        snack_name = choice

    # Need to remove white space from around snack
    snack_name = snack_name.strip()
    return quantity_required, snack_name


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry that is not a valid choice "
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Function to collate each other
def collate_order():
    # valid snacks holds list of all snacks, each item is itself a list with
    # all the acceptable input options for each snack - full name, initials and
    # abbreviations, as well as a reference number
    valid_snacks = [["popcorn", "p", "corn", "(1"],
                    ["m&ms", "mms", "m", "mm", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "w", "(4"], ["orange juice", "oj", "(5"],
                    ["x", "exit", "(6"]]

    # Valid options for yes/no questions
    valid_yes_no = [["y", "yes"], ["n", "no"]]

    # the snack order list records the complete order for a single order
    snack_order = []


    # Maximum number of any snack item which can be ordered
    max_number_of_snacks = 4

    # Assumption that every user will want to order snacks
    getting_snacks = True
    while getting_snacks:
        # Firstly, find out whether the user will want to order snacks
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            # Response is passed to the generic string checking function with the
            # list of valid yes/no responses as parameters
            check_snacks = input("Do you want snacks? (Y/N): ").lower()
            snacks_required = get_choice(check_snacks, valid_yes_no)

        if snacks_required == "N":  # But if they don't want any snacks
            getting_snacks = False  # Break the while loop
            break

        else:
            # otherwise, for each snack, the generic string checker is called with
            # the ask_for_snacks question and the list of valid snacks as
            # parameters
            option = ""
            while option != "X":
                snack = input("What snack do you want - or 'x' to stop "
                              "ordering ").lower()
                snack = split_order(snack)
                quantity = snack[0]
                if quantity > max_number_of_snacks:
                    snack = None
                    print("Sorry, the maximum number you can order is 4 ")
                else:
                    snack = snack[1]
                    option = get_choice(snack, valid_snacks)
                    if option == "X":
                        getting_snacks = False

                    elif option is not None:  # Filters out invalid choices
                        snack_order.append([quantity, option])
    return snack_order


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
        snack_order = collate_order()
        # print(snack_order)

        # after the loop is broken, check for an emtpy list
        if len(snack_order) > 0:  # if there is something in the list, print each item
            print("\nThis is a summary of your order: ")
            for item in snack_order:
                print(f"\t{item[0]} {item[1]}")
        else:  # otherwise, print this
            print("No snacks were ordered")
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

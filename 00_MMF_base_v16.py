"""Based on 00_MMF_base_v14

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
                    ["water", "h20", "w", "(4"],
                    ["orange juice", "o", "oj", "juice", "(5"],
                    ["x", "exit", "(6"]]

    # the snack order list records the complete order for a single order
    snacks_order = []

    # Maximum number of any snack item which can be ordered
    max_number_of_snacks = 4

    option = ""
    while option != "X":
        snack = input("What snack do you want - qty then item"
                      "\n e.g. '2 popcorn' OR - 'x' to stop "
                      "ordering: ").lower()
        snack = split_order(snack)
        quantity = snack[0]

        if quantity > max_number_of_snacks:
            print("Sorry, the maximum number you can order is 4")
        else:
            snack = snack[1]
            option = get_choice(snack, valid_snacks)
            if option == "X":
                break
            elif option is not None:  # Filters out invalid choices
                snacks_order.append([quantity, option])
    return snacks_order


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
    valid_age = number_checker(f"Please enter {name}'s age: ")
    if valid_age < minimum:
        print(f"Sorry, {name} is too young for this movie")
        return None
    else:
        while not valid_age <= maximum:  # age must be between 12 and 110
            valid_age = number_checker(f"\nAt {valid_age} {name} is very old. "
                                       f"Please re-enter {name}'s age: ")
        return valid_age


def check_valid_payment_method():
    ask_payment_method = input("How do you want to pay: ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"],
                            ["cash", "ca", "money", "notes", "coins", "c",
                             "3"]]
    payment_method = get_choice(ask_payment_method, valid_payment_method)
    return payment_method


def ticket_counting(tickets_sold, maximum):
    if ticket_count < MAX_TICKETS:
        if ticket_count > 1:  # Making sure it reads OK when only
            # one ticket sold
            print(f"\n{ticket_count} tickets have now been sold")
        else:
            print(f"1 ticket has now been sold")
        if MAX_TICKETS - ticket_count > 1:
            print(f"{MAX_TICKETS - ticket_count} tickets are still "
                  f"available\n")
        else:
            print("1 ticket is still available\n")  # Making sure is reads
            # ok when only one ticket is left

    else:
        print("\n!!!!!!!!All available tickets have now been sold!!!!!!!!")
        print("*" * 60)


# Currency formatting function
def currency(number):
    return f"${number:,.2f}"


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = not_blank("Would you like to read the "
                                 "instructions?: ").lower()
        instructions = (get_choice(instructions, valid_responses))

    if instructions == "Y":
        print("\n **********************************************************\n"
              "\t\t*** Mega Movie Fundraiser Instructions ***\n"
              "You will be shown how many tickets are still available\n"
              "for sale and asked for the first ticket-purchaser's name.\n"
              "You will then be asked to input the ticket-purchaser's age.\n"
              "\n This is because:\n"
              "\t- the minimum age for entry is 12; and\n"
              "\t- there is standard price for adults; but\n"
              "\t- different prices for students and retired people\n"
              "\n the program will then ask you for the snacks required\n"
              "and once these are entered you will need to provide\n"
              "a valid method of payment\n"
              "This process keeps repeating until either all tickets are\n"
              "sold or you choose to exit the program.\n"
              "\nOn exit, a summary of profits and sales will be printed to\n"
              "the screen. Full details of all sales and profits are also\n"
              "output to .csv files. These can be found in the same\n"
              "dictionary in which the program is stored.\n"
              "\n***********************************************************\n")
    print("Program launches...")


# ********  main routine  ********

# set up dictionaries / list needed to hold data
all_names = []
all_tickets = []

# Create separate lists for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

# Put the separate lists above into a master list
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Store surcharge multiplier
surcharge_mult_list = []

# Lists to store summary data
# Heading order matches the lists in te 'snacks_lists' master list above
summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water", "Orange Juice",
                    "Snack Profit", "Ticket Profit", "Total Profit"]

# Empty list to hold the data for above summary
summary_data = []

# Dictionary to hold summary information
summary_data_dict = {
    "Item": summary_headings,
    "Amount": summary_data
}
# Data Frame Dictionaries / lists needed to hold data
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice,
    "Surcharge Multiplier": surcharge_mult_list
}

# cost of each snack
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
}
SNACK_PROFIT_MARGIN = .2
SURCHARGE_RATE = .05
MINIMUM_AGE = 12
MAXIMUM_AGE = 110
MAX_TICKETS = 150
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
ticket_profit = 0
surcharge = 0


# Ask user if they have used the program before and
# show instructions if necessary
print("*** Welcome to Mega Movie ***")

# Valid options for any yes/no questions
valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)


# loop to get ticket details
# Initialise loop so that is runs at least once

while name != "X" and ticket_count < MAX_TICKETS:
    # Check to ensure there are still tickets left
    check_max_tickets(MAX_TICKETS, ticket_count)

    # Get details
    # Get name
    name = not_blank("Enter ticket-holders name: ").title()
    # name can't be blank
    if name == "X":
        break
    else:
        # Check for a valid age and then calculate ticket price
        age = check_valid_age(MINIMUM_AGE, MAXIMUM_AGE)
        if not age:
            continue  # restarts the get tickets loop
        else:
            ticket_count += 1  # Don't want to include escape code in
            # the ticket_count

        # Calculate ticket price
        ticket_price = calculate_ticket_price(age)
        print(f"For {name} the price is ${ticket_price:,.2f}")

        # Add name and ticket price to lists
        all_names.append(name)
        all_tickets.append(ticket_price)

        # Calculate ticket profit and add to running total
        ticket_profit += (ticket_price - TICKET_COST_PRICE)

        # get snacks
        snack_order = collate_order()

        # Assume no snacks have been bought
        for item in snack_lists:
            item.append(0)  # add 0 as the amount for each item

        # print(snack_order)
        for item in snack_order:  # The item only has 2 parts - number and
            # snack
            if len(item) > 0:  # checking to eliminate any blank orders
                to_find = item[1]  # gets the snack name for the item ordered
                amount = item[0]  # amd sets 'amount' to number ordered
                add_list = movie_data_dict[to_find]  # Matches the snack name
                # to the movie_menu_dict
                add_list[-1] = amount  # Appends the number ordered to the end
                # of the dictionary list of quantities ordered eg if the most
                # recent quantity is 3 it would be added to the end of
                # this list: [2, 5, 0, 1, 3]

        # after the loop is broken, check for an emtpy list
        if len(snack_order) > 0:  # if there is something in the list, print
            # each item
            print("\nThis is a summary of your order: ")
            for item in snack_order:
                print(f"\t{item[0]} {item[1]}")
        else:  # otherwise, print this
            print("No snacks were ordered")

        # Get payment method (and work out surcharge as necessary)
        payment_method = check_valid_payment_method()
        while not payment_method:
            payment_method = check_valid_payment_method()

        if payment_method == "Credit Card":
            surcharge_multiplier = SURCHARGE_RATE

        else:
            surcharge_multiplier = 0

        surcharge_mult_list.append(surcharge_multiplier)

        ticket_counting(ticket_count, MAX_TICKETS)

    # End of tickets/snacks/payment loop


# print details
print()

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")  # Changes the index to reference

# Calculate the collective price of snacks ordered
movie_frame["Snack Cost"] = \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Sub Total"] = movie_frame["Snack Cost"] + movie_frame["Ticket"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame["Surcharge"]

# Shorten column names
movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips",
                                          "Surcharge Multiplier": "SM"})

# set up summary data frame
# Populate snack item from the master snack_list
for item in snack_lists:
    # Sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame["Snack Cost"].sum()
snack_profit = snack_total * SNACK_PROFIT_MARGIN


# Work out total profit and add to list
total_profit = snack_profit + ticket_profit
# Format profit figures and ad dto summary list
currency_amounts = [snack_profit, ticket_profit, total_profit]
for amount in currency_amounts:
    amount = currency(amount)
    summary_data.append(amount)

# Creates the summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index("Item")

# force all columns to be printed
pandas.set_option("display.max_columns", None)

# **** Pre Printing / Export ****
# Format currency values so they have $'s
currency_amounts = ["Ticket", "Snack Cost", "Sub Total", "Surcharge", "Total"]
for amount in currency_amounts:
    movie_frame[amount] = movie_frame[amount].apply(currency)  # this is a call
    # to the currency() function above

# Write each frame to separate csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")


# printing the abbreviated table
print()
print("*** Ticket/Snack Information ***")
# Refers to an export file - functionality yet to be developed
print("Note: for full details please see the excel file called "
      "snack_summary.csv and ticket_details.csv")
print()
print(movie_frame[["Ticket", "Snack Cost", "Sub Total", "Surcharge", "Total"]])
print()

# printing the summary frame
print("*** Snack/Profit Summary ***")
print()
print(summary_frame)

# Remaining tickets
ticket_counting(ticket_count, MAX_TICKETS)


# output data to text file

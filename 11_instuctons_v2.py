"""This component is based on v1
Puts the component into it's own function
This version includes actual instructions
"""


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


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Checks that the ticket name is not blank
def not_blank(question):
    valid = ""
    while not valid:
        response = input(question).lower()

        # If the name is blank, it shows this error message
        if not response.isalpha():
            print("\n You can't include digits or leave this blank...")
        else:
            return response  # but if name is not blank, program continues


# Main routine
# Valid options for any yes/no questions
valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)

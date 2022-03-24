"""includes testing loop
this component, originally designed to ask if the user wants to purchase
snacks, asks for a yes/ no response and keeps asking - for the purpose of
testing. in this version the porgram makes a decision based in the first
letter of hte response
"""


def yes_no_response(question):
    error_message = "Please answer 'Y' or 'N'"
    valid_response = ["y", "yes", "n", "no"]
    response = input("Do you want snacks? ").lower()
    while response not in valid_response:
        print(error_message)
        response = input("Do you want snacks? ").lower()

    if response[0] == "n":
        return False
    else:
        return True


# main routine
# temporary input statements - during development
testing = True
while testing:
    snacks_required = yes_no_response("Do you want snacks? ")
    if not snacks_required:
        print("Valid answer. You don't want snacks")
    else:
        print("Valid answer. You do want snacks")
    print()

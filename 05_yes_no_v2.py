"""This component asks for a Yes/No response and keeps asking until a valid
response is provided.
"""


def yes_no_response(question):
    error_message = "Please answer 'Y' or 'N'"
    valid_response = ["y", "yes", "n", "no"]
    response = input("Do you want snacks? ").lower()
    while response not in valid_response:
        print(error_message)
        response = input("Do you want snacks? ").lower()

    if response == "n" or response == "no":
        print("Valid answer. you don't want snacks")
    else:
        return True


# main routine
# temporary input statements - during development
snacks_required = yes_no_response("Do you want snacks? ")
if not snacks_required:
    print("Valid answer. You don't want snacks")
else:
    print("Valid answer. You do want snacks")

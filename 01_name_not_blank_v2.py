def not_blank(question, error_message):
    vaild = ""
    while not vaild:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# main routine
name = not_blank("Whats your name: ", "You can't leave this blank...")

def not_blank(question):
    vaild = ""
    while not vaild:
        response = input(question)
        if not response:
            print("You can't leave this blank...")
        else:
            return response


# main routine
name = not_blank("Whats your name: ")

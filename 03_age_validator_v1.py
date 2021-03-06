# integer checking function - first trial method

def integer_checker(question, low_num, high_num):
    error = f"Please enter an integer that is between{low_num} and {high_num}"
    vaild = False
    while not vaild:
        #  asking user for a number and check to see if it is vaild
        try:
            number_to_check = int(input(question))
            if low_num <= number_to_check <= high_num:
                return number_to_check
            else:
                print(error)
        except ValueError:
            print("\nPlease enter and integer (ie a whole number"
                  " with not decimals)")


# Main Routine
# Check for a valid age - must be between 12 and 110
age = integer_checker("\nPlease enter the age of the ticket-holder: ", 12, 110)
print(f"Age = {age}")

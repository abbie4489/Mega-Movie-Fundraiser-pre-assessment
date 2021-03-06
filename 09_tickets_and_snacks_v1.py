"""Based on 08_initialise_snack_lists_v2
Add tickets list-for testing purposes (names/ticket prices match the test plan)
Add the ticket list to the movie_data_dict
Create a price dictionary
Remove the print statements under "# Print snack lists" at the bottom of this
code and replaced them with the 'sub total' block
Shorten the column names in the frame - to make them better fit
"""
import pandas

names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]
tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

# Create separate lists for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

# put the separate lists above into a master list
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Creating the snack dictionary with a label and then the list for content
movie_data_dict = {
    "Name": names,
    "Ticket": tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice
}
# cost of each snack
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
}
# Data for testing the printing routine below
test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],  # this is for Manaia's order - she ordered nothing
    [[1, 'Water']],
    [[1, 'Popcorn'], [1, 'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0  # Need count to get the index number of each item in the snack_order
for client_order in test_data:  # Going through each order
    # Assume no snacks have been bought
    for item in snack_lists:
        item.append(0)  # add 0 as the amount for each item

    # Print (snack lists)
    snack_order = test_data[count]  # sets snack_order to the
    # [count value of index] item in test data
    count += 1

    for item in snack_order:  # The item only has 2 parts - number and snack
        if len(item) > 0:  # checking to eliminate any blank orders
            to_find = item[1]  # gets the snack name for the item ordered
            amount = item[0]  # amd sets 'amount' to number ordered
            add_list = movie_data_dict[to_find]  # Matches the snack name to
            # the movie_menu_dict
            add_list[-1] = amount  # Appends the number ordered to the end of
            # the dictionary list of quantities ordered eg if the most recent
            # quantity is 3 it would be added to the end of
            # this list: [2, 5, 0, 1, 3]

print()

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")  # Changes the index to reference
movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

# Shorten column names
movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips"})
# the names rather than an actual index number
print(movie_frame)

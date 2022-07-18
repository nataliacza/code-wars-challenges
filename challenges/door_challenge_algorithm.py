"""In a row there is a line of 100 doors. You can open or close door. All doors are closed at the beginning.
After 1st passing, you open every door.
After 2nd passing, you open or close every 2nd door. => change status of door
After 3rd passing, you open or close every 3rd door. => change status of door
etc"""


# "close" = False
# "open" = True

# This is separate method to create a dictionary
def create_dictionary(elements):
    """door_dict = {}
    for i in range(1, 101):
        door_dict[i] = False
    return door_dict"""
    return {k: False for k in range(1, elements + 1)}


# A method to change status/value of an element
def switch_status(value):
    if not value:
        return True
    return False

# Main logic
def open_close_challenge():
    my_dict = create_dictionary(100)
    for i in my_dict:
        for k, v in my_dict.items():
            if k % i == 0:
                my_dict[k] = switch_status(v)
    return my_dict

# And let's call the method to debug
open_close_challenge()

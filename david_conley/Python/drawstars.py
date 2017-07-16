# create a function called draw_starts that takes a list of numbers and prints out *

def draw_stars(list):
    for item in list:
        print "*" * item
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

# Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

def draw_stuff(list):
    for item in list:
        if type(item) is str:
            string = item[0] * len(item)
            print string.lower()

        if type(item) is int:
            print "*" * item

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stuff(x)

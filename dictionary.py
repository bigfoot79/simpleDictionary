# create a simple dictionary list (sample code only)
# Written by Vince, started 20/09/2018

# version 1.0       20/09/2018   Vincent     Initial program code

# import declarations


# function/block declarations
def add_elements(items):

    items["jargon"] = "The technical terms used by experts in their chosen field"
    items["dictionary"] = "The list of elements and their corresponding meaning"
    items["environment"] = "The ecosystem encompassing the system described"

    return(items)

def main():
    # this program simply creates a dictionary (2 element list) and then identifies if an element exists and returns the keyValue phrase.
    items = {}
    add_elements(items)

    print("Jargon definition: %s" % items["jargon"])
    print("Dictionary definition: %s" % items["dictionary"])
    print("Environment definition: %s" % items["environment"])


if __name__ == '__main__':

    main()
    print("Program complete")




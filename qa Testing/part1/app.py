blogs = dict()  # blog name to blog object OneToOne relation


def manu():
    # show the user available blogs
    # let the user maka a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()


def print_blogs():
    "Print available blogs"
    for keys, values in blogs.items():
        print(f"{keys} - {values}")

from blog import Blog

""""
show the user the available blogs
let the user make a choice
Do something with that choice
Eventually Exit

"""
MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one,
'p' to create a post, or 'q' to quit."

blogs = dict()


def menu():
    pass

    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print("-Test by Test Author (0 posts)")

# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple key-word arguments
#             * unpacking operator
#             1. positional, 2. default, 3. keyword, 4. ARBITRARY
def args_demo(*args):
    print(type(args))
    for i in args:
        print(i)


def kwargs_demo(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}:{value}")


# exercise, using them together
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")

    print()

    # for value in kwargs.values():
    #     print(value, end=" ")
    #

    if "apt" in kwargs:
        print(f"{kwargs.get('street') }{kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('street')}")


if __name__ == '__main__':
    # args_demo("maron","cazmir","jamille")
    # kwargs_demo(
    #     first_name="ralphmaron",
    #     last_name="eda"
    # )

    shipping_label(
        "Engr.", "Ralph Maron", "Eda",
        street="123 Hello St.",
        apt="100",
        city="Detroit",
        state="MI",
        zip="54321"
    )

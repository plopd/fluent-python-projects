"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

    Example 7-14. Calculate a running average without keeping all history (fixed with the use of nonlocal)
"""

def make_averager():
    avg = 0
    i = 0

    def averager(new_value):
        # flag the variable as a free variale,
        # thereby binding it to the closure.
        nonlocal avg, i
        i += 1
        avg += 1/i*(new_value - avg)

        return avg

    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg.__closure__)
    print(avg.__code__.co_freevars)
    print(avg(10))  # 10.
    print(avg.__closure__[0].cell_contents)
    print(avg(11))  # 10.5
    print(avg.__closure__[0].cell_contents)
    print(avg(12))  # 11.
    print(avg.__closure__[0].cell_contents)


"""
    * For all immutable types, such as integers,
    += means assignment. So without the nonlocal assignment,
    we are effectively making `avg` and `i` local.
    But since we never defined them, += will raise an error.
"""
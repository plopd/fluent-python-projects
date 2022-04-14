"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

    Example 7-9. average.py: A higher-order function to calculate a running average
"""

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

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

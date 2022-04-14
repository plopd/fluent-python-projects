"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

    Example 7-8. average_oo.py: A class to calculate a running average
"""

class Averager():

    def __init__(self):
        self._avg = 0
        self._i = 0

    def __call__(self, new_value):
        self._i += 1
        self._avg += 1/self._i*(new_value - self._avg)
        return self._avg

if __name__ == "__main__":
    avg = Averager()
    print(avg(10))  # 10.
    print(avg(11))  # 10.5
    print(avg(12))  # 11.

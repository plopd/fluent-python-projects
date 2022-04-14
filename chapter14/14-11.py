"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""

"""
Example 14-11. The Arithmetic Progression class.

    The Iterator pattern allows for traversal of a data structure.
But the same interface can be used to fetch the next item in a series,
produced on the fly (e.g., the `range` built-in).
"""

class ArithmeticProgression:
    """
        Arithmetic Progression(begin, step[, end])
    """

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None --> infinite series

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

ap = ArithmeticProgression(0, 1, 3)
print(list(ap))  # [0, 1, 2]

ap = ArithmeticProgression(0., 1, 3)
print(list(ap))  # [0., 1., 2.]

from decimal import Decimal
ap = ArithmeticProgression(0, Decimal('0.5'), 3)
print(list(ap))  # [0., 0.5, 1.0, 1.5, 2.0, 2.5]

import itertools
def aritprog_gen(begin, step, end=None):
    """
        A standard Python function that returns a generator.
        So it can be well taught of as a generator factory.
    """
    start = type(begin + step)(begin)
    ap_gen = itertools.count(start, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    
    return ap_gen

# `ArithmeticProgression` can be written succintly using
# itertools.takewhile, that takes in a generator and produces
# another generator until a condition evaluates to False.
assert list(ap) == list(aritprog_gen(0, Decimal('0.5'), 3))

ap = ArithmeticProgression(0, 1)
# Loop runs forever but we cap it after 11 steps
for i, num in enumerate(ap):
    print(num)
    if i == 10:
        break
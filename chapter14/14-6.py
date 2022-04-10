"""
    Example 14-6. A generator function that prints messages when it runs.
"""

def gen_AB():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end.")

g = iter(gen_AB())
print("-->", next(g)) # start --> A
print("-->", next(g)) # continue --> B
print("-->", next(g)) # end.
print("-->", next(g)) # StopIteration

"""
    Each next executes the code until (and including) the first yield,
from the previous yield.
Above we simulated the for-loop machinery, by:
* making g a generator
* calling next repeatedly to yield the values.
"""
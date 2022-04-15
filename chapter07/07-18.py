"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

Example 7-18. The very costly recursive way to compute the nth number in the Fibo‐ nacci series
"""
import functools
from clockdeco import clock

@functools.lru_cache(maxsize=128, typed=False)
@clock
# Note that all the arguments of the decorated function
# must be hashable if you apply the `lru_cache` decorator,
# because `lru_cache` stores the cache internally in a dictionary.
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    print(fibonacci(100))

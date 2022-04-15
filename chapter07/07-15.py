"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

    Example 7-15. A simple decorator to output the running time of functions
"""
import time
import functools

def clock(func):
    """This is a simple decorator function."""
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        """This is a closure function that extends the output of a function with its running time."""
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%s' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))

        return result
        
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n, foo='bar'):
    """This function computes the factorial in a recursive way of any natural number."""
    return 1 if n < 2 else n*factorial(n-1, foo='bar')


if __name__ == "__main__":
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    # functools.wraps is a helper built-in 
    # that makes it possible to get the right name and doc of a decorated function.
    # Without it, if we want the name and doc of factorial,
    # we would instead get the name and docstring of `clocked`.
    print(factorial.__name__)  # factorial
    print(factorial.__doc__)   # This function computes the factorial in a recursive way of any natural number.

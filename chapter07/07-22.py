"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

Example 7-22. Abridged registration.py module from Example 7-2, repeated here for convenience
"""

registry = set()

def register(active=True):
    """A parametrized decorator factory."""
    def decorate(func):
        """The actual decorator of `func`"""
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register()
def f1():
    print('running f1()')

@register(active=False)
def f2():
    print('running f2()')

def f3():
    print('running f3()')

if __name__ == "__main__":
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    # This is an equivalent way to what the parameterized decorator is doing.
    register(active=True)(f3)
    f3()
"""
    Source: “Fluent Python by Luciano Ramalho (O'Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""

class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Do not divide by zero.')
            return True

if __name__ == "__main__":

    with LookingGlass() as what:
        print("How long is forever? Sometimes just one second")
        print(what)
    print(what)

    print("Alternative way of using a context manager without with")

    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    # Every std.out is mirrored!
    print(monster == "JABBERWOCKY")
    print(monster)
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)  # Back to normal
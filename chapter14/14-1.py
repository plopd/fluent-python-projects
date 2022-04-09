# Example 14-1 shows a Sentence class that extracts words from a text by index.

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    # Either `__getitem__` or `__iter__` must be implemented,
    # to make an Iterable. If not, Python will throw a:
    # TypeError: `Sentence` object is not iterable
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('"Nobody ever figures out what life is all about"')
# reprlib is printing a abbreviated form
print(s) # Sentence('"Nobody ever...is all about"')

# Sentence is a generator so you can yield words from the sentence
try:
    for word in s:
        print(word)
except TypeError as e:
    print("Oh-oh. Does Sentence implement __getitem__ or __iter__ ?")
    print(e)
    exit(1)

# cast generator to list and print it all at once
print(list(s))

# Sentence is also a sequence, so you can index it.
print(s[0])
print(s[-1])


# Iterators are obtained _from_ iterables:
s = 'ABC'
print("s is an Iterable: %s" % hasattr(s, '__iter__')) # True
print("s is an Iterator: %s" % hasattr(s, '__next__')) # False
it = iter(s)
print("it is an Iterator: %s" % hasattr(it, '__next__')) # True

while True:
    try:
        print(next(it)) 
    except StopIteration:
        print("Reached the end of the string.")
        del it
        break

# The standard interface of an Iterator has two methods:
# `__next__` and `__iter__`

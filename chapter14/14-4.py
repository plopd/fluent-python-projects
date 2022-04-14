"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""
# Example 15-4. sentence_iter.py: Sentence implemented using the Iterator pattern
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1   
        return word

    # For this example, it is not needed to implement it,
    # but it's the right thing to do:
    # Iterators are supposed to implement both
    # `__next__` and `__iter__`
    def __iter__(self):

        return self

s = Sentence('"Nobody ever figures out what life is all about"')

for word in s:
    print(word)
"""
    Iterables have `__iter__` method that instantiates
a new iterator every time.
Iterators implement a `__next__` method that returns invididual
items, and an `__iter__` method that returns self.
==> Iterators are iterables, but iterables are not iterators.
Therefore, an iterable must implement `__iter__`, 
but not _never_ implement `__next__`.
"""
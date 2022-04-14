"""
    Modified
    Example 14-5. sentence_gen.py: Sentence implemented using a generator function.
"""

import re
import types
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # By using a generator here we are replacing
    # the SequenceIterator implementation from 14-4.
    def __iter__(self):
        for word in self.words:
            yield word

    
s = Sentence('"Nobody ever figures out what life is all about"')
for word in s:
    print(word)
print(isinstance(iter(s), types.GeneratorType))

"""
    Here, `__iter__` of Sentence is a generator.
In general, any function that has `yield` in its body is a generator.
Generators are iterators that produce the values of the expressions
passed to it.
It's confusing to say a generator "returns" values.
Functions return values. Generators yield or produce values.
The return statement of the generator raises a StopIteration
when there is no more element to yield.
"""
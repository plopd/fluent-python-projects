"""
    Example 14-7. Sentence implemented using a generator function calling the re.finditer generator function.
"""

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

s = Sentence('"Nobody ever figures out what life is all about"')
for word in s:
    print(word)
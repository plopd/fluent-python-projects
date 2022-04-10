"""
    Example 14-9.: Sentence implemented using a generator expression.
"""

import re
import reprlib

RE_WORD=re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


s = Sentence('"Nobody ever figures out what life is all about"')
for word in s:
    print(word)
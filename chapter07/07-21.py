"""
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

Example 7-21. singledispatch creates a custom htmlize.register to bundle several func‐ tions into a generic function
"""
from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

# The specialized function is decorator with `@base_function.register(type)`
# The name of the function is arbitrary. `_` is a good candidate,
# since it makes it clear that all these functions here are handling `hmtlize`
# in their own specialized way.
@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(list)
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

if __name__ == "__main__":
    print(htmlize({1,2,3}))
    print("-"*30)
    print(htmlize(42))
    print("-"*30)
    print(htmlize(['alpha', 66, {1,2,3}]))
    print("-"*30)
    print(htmlize([1,2,3]))
    print("-"*30)
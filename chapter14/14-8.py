"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""

"""
    Example 14-8. The gen_AB generator function is used by a list comprehension, then by a generator expression.
"""

def gen_AB():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end.")

res = [x for x in gen_AB()]

for i in res:
    print("-->", i)

res = (x for x in gen_AB())
print(res)

for i in res:
    print("-->", i)

"""
    A generator can be thought of as a lazy-loading list comprehension.
"""
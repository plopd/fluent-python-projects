"""
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""

## Listcomps No Longer Leak Their Variables

x = "ABC"
# Variables in the surrounding scope can still be referenced
dummy = [ord(x) for x in x]
# The x inside the listcomp does not mask the x in the surrounding scope
print(x) # ABC
print(dummy)  # [65, 66, 67]

## Listcomps Versus map and filter
## Example 2-3. The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii) # [162, 163, 165, 8364, 164]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii) # [162, 163, 165, 8364, 164]

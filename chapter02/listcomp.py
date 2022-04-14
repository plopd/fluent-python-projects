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


## Cartesian Products
## Example 2-4. Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors 
                            for size in sizes]
print(tshirts) # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]


## Generator Expressions
## Example 2-5 shows basic usage of genexps to build a tuple and an array
symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))  # (36, 162, 163, 165, 8364, 164)
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))  # array('I', [36, 162, 163, 165, 8364, 164])

# Example 2-6. Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# Example 2-7 Tuple as Records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
travel_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(travel_ids):
    print('%s/%s' % passport)

for country, _ in travel_ids:
    print(country)

# Some cool stuff with tuple unpacking

# Parallel tuple unpacking using * notation to grab the excess.
# Note that only one item can have the *, but it may appear in any position of the unpacking.
a, b, *rest = range(2)
print(a, b, rest) # 0, 1, []


# Example 2-8. Unpacking nested tuples to access the longitude
metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print("{:15} | {:^9} | {:^9}".format("city", "lat.", "long."))
print("-"*42)
fmt = "{:15} | {:9.4f} | {:9.4f}"
for city, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(city, latitude, longitude))

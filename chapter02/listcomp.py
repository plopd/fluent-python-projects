
x = "ABC"
# Variables in the surrounding scope can still be referenced
dummy = [ord(x) for x in x]
# The x inside the listcomp does not mask the x in the surrounding scope
print(x) # ABC
print(dummy)  # [65, 66, 67]
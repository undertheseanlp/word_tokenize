import re

print re.search(r" $", "c ")  # found
print re.search(r" $", "c")  # None
print re.search(r" $", "d d")  # None

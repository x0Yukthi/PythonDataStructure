# To get the number of occurrences of a specified element in an array

import array as a

ar = a.array('i', [34, 67, 84, 67, 80, 32, 54])
print('Occurence of 67 -> ', ar.count(67))

c, m = 0, 67
for x in ar:
    if x == m:
        c = c + 1

print('Occurence -> ', c)

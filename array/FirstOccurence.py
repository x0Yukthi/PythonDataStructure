# to remove the first occurrence of a specified element from an array.

import array as a

b = a.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
b.remove(3)
print('After Deletion of 1st occurence of 3 -> ', b)


def first_deletion(c, i):
    for x in c:
        if x == i:
            c.remove(1)
            break

    print('After Deletion of 1st occurence of 1 -> ', c)


c = a.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
d = 1
first_deletion(c, d)

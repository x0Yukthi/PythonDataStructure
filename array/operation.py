# array in python
import array as arr

# to create
a = arr.array('d', [1, 2, 3])
print(a)

# accessing
print(a[0])

# basic operation
# adding
a.append(33)
print('append -> ', a)

a.extend([45, 67, 89])
print('extend -> ', a)

a.insert(100, 30)
print('insert -> ', a)

# length of array

print('Length -> ', len(a))

# remove/delete
print('pop -> ', a.pop())
print('pop@2 ->', a.pop(2))

a.remove(89)
print('After deletion -> ', a)

# slicing
print('Using Slicing -> ', a[1:3])

# looping
print('To print all array elements -> ')
for x in a:
    print(x)
print('To print specific values')
for x in a[0:3]:
    print(x)

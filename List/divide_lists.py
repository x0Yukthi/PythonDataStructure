'''A program to divide the list into chunks of size n'''

mylist = [45, 87, 85, 1, 5, 10, 66, 49, 91, 25, 37, 70]
print('The list:\n', mylist)
n = int(input('\nEnter the how many element each list should have:\n'))

print('\nThe chunks of length {} are \n'.format(n))
for i in range(0, len(mylist), n):
    lst = mylist[i:i + n]
    print(lst)

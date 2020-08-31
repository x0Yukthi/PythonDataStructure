'''Reverse a given list'''
'''a fuction to reverse list'''


def toReverse(lst):
    newList = []
    newList = lst[::-1]
    return newList


myList = []
# size of list
n = int(input('Enter the length of list:\n'))
for i in range(n):
    ele = int(input('Enter {} element\n'.format(i)))
    myList.append(ele)

print('Before revering the list :\n', myList)
print('\nList after reversing :\n', toReverse(myList))

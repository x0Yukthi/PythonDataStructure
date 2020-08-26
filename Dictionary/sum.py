'''A program to find the sum of all values in a dictionary!!'''
print("Program to find sum of all items in dictionary!!")


def toFindSum(myD):
    s = 0
    for i in myD.values():
        s= s + i
    print('Sum:{}'.format(s))


d = dict()
length = int(input('Enter the number of {key:value} pairs\n'))
for i in range(length):
    Input = input('\nEnter the {key:value} pair\nThe input should be of the format key:value\n')
    t = Input.split(':')
    d[t[0]] = int(t[1])

toFindSum(d)

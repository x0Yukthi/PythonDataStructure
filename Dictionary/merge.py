'''Merging two dictionaries'''

'''A single line expression'''


def toMerge(t1, t2):
    res = {**t1, **t2}
    print('After merging the two dictionaries\n')
    print(res)


d1 = dict()
d2 = dict()
print("To merge enter two dictionaries\n")
len1, len2 = input('Enter the length for both dictionaries:').split()
print("\nEnter the 1st dictionary\n")
for i in range(int(len1)):
    data1 = input('Enter the {key:value} pair\nThe input should be of the format key:value\n')
    t = data1.split(':')
    d1[t[0]] = int(t[1])
print("\nEnter the 2nd dictionary\n")
for i in range(int(len2)):
    data2 = input('Enter the {key:value} pair\nThe input should be of the format key:value\n')
    t = data2.split(':')
    d2[t[0]] = int(t[1])
'''call to the function toMerge'''
toMerge(d1, d2)

'''Using the built-in fuction to merge'''
print("\nUsing update() to merge 2 dictionaries\n")
d1.update(d2)
print(d1)

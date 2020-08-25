'''A program to find the number of even and odd in a list'''


# fuction to find the count of odd and even in given list.
def tofindcount(lst, s):
    ocount = 0
    ecount = 0
    for i in lst:
        if (i % 2 == 0):
            ecount += 1
        else:
            ocount += 1
    print("Even count in list : ", ecount)
    print("Odd count in the list:", ocount)


print("To find the number of even and odd\n")
mylist = []
l=int(input("Enter the size of the list\n"))
for i in range(0, l):
    ele =int(input("enter the {0} value:\n".format(i)))
    mylist.append(ele)
print(tofindcount(mylist,l))

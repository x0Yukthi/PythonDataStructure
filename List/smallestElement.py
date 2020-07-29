# Gives the smallest in list

def smallest(list):
    m = list[0]
    for i in range(len(list)):
        if list[i] < m:
            m = list[i]
    return m


mylist = []
l = int(input("Enter the length \n"))
for i in range(0, l):
    ele = int(input("enter the {0} element ".format(i)))
    mylist.append(ele)

print(mylist)
print("\nSmallest in the list :", smallest(mylist))

# using min() to find smallest
print("\nSmallest in the list using min() :", min(mylist))

# using sort() to find smallest

mylist.sort()
print("\nsmallest in the list using sort() :", mylist[0])

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
print("Smallest in the list :", smallest(mylist))

# using sort() to find smallest

mylist.sort()
print("smallest in the list using sort() :", mylist[0])

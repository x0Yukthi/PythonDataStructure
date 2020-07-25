# to check the existence of element in the list

f = 0
Mylist = list(input("Enter the elements of list\n"))
ele = input("Enter the element to be searched\n")
for i in Mylist:
    if i == ele:
        print(ele + " exist\n")
        f = 1
if f == 0:
    print(ele + " does not exist\n")
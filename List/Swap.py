# To swap first and last element in a list


newlist = list(input("Enter the elements of list\n"))

newlist[0], newlist[-1] = newlist[-1], newlist[0]

print(newlist)

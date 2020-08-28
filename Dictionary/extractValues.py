'''A program to extract the values of a perticular key from nested dictionary'''

D = {
    "D1": {"1": 4, "a": 67, "2": "dictionary0", "b": 864, "3": "Lists"},
    "D2": {"1": 547, "a": "hello", "2": 57895, "b": 2464, "3": "World"},
    "D3": {"1": "Python", "a": 54.234, "2": "Java", "b": "C++", "3": "Ruby"}
}
print("The nested Dictonary is:\n", str(D))
ele = input("Enter the key hows values are to be extracted:\n")
# noinspection PyUnboundLocalVariable
newDict = dict(D)

r = [sub[ele] for sub in newDict.values() if ele in sub.keys()]

print("The values of {} are: {}".format(ele, r))

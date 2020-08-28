'''A program to extract the values of a particular key from nested dictionary'''

D = {
    "D1": {"1": 4, "a": 67, "2": "dictionary0", "b": 864, "3": "Lists"},
    "D2": {"1": 547, "a": "hello", "2": 57895, "b": 2464, "3": "World"},
    "D3": {"1": "Python", "a": 54.234, "2": "Java", "b": "C++", "3": "Ruby"}
}
print("\nThe nested Dictionary is:\n", str(D))
ele = input("\nEnter the key whos values are to be extracted:\n")

# loop to find the values of key
r = [sub[ele] for sub in D.values() if ele in sub.keys()]

# to print the extracted values of key
print("\nThe values of {} are : {}".format(ele, r))

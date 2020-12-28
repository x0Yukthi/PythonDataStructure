#To reverse a given array
import array as arr
#using library
a= arr.array('d',[1,2,3,4,5])
a1 = a[::-1]
print('Array Reversal -> ',a1)


b = [1,2,3,4]
b1 = b[::-1]
print('array reverse ->',b1)

#reverse using reversed()
c = [52.5,78.9,63.7,935.9]
c.reverse()
print("Reversed array ->",c)
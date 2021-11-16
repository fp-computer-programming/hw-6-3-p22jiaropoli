# Author JRI 11/15/21

x = list(input("Enter numbers in list order "))

x2 = x.copy()
x2.sort()

if x == x2:
    print("The list is sorted ")
else:
    print("The list is not sorted ")
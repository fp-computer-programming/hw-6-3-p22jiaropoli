# Author JRI 11/15/21

x1 = list(input("Please enter a word "))
x2 = list(input("Please enter a second word "))

x1.sort()
x2.sort()

if x1 == x2:
    print("These two words are anagrams ")
else:
    print("These two words are not anagrams ")

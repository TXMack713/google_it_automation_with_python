#!/usr/bin/env python3

# Google IT Automation with Python - Testing, Jupyter Practice Labs 1 & 2

my_list = [27, 5, 9, 6, 8]
print("Original list: " + str(my_list))
def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("The entry is not available in the list of values.")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

# Call the function a second time with the same value to verify that the raise exception handling works
# print(RemoveValue(27))

my_word_list = ['east', 'after', 'up', 'over', 'inside']
my_new_list = [6, 3, 8, "12", 42]
def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "List must only contain string entries"
    myList.sort()
    return myList

print(OrganizeList(my_word_list))
# Call the function a second time with a mixed list to verify that the assert exception handling works
# print(OrganizeList(my_new_list))


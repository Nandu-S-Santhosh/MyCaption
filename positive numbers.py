
# Python program to print positive Numbers in a List

# list of numbers
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
#merging each element of both lists
list3=list1+list2
# iterating each number in list
for num in list3:
    # checking condition
    if num >= 0:
       print(num, end = " ")

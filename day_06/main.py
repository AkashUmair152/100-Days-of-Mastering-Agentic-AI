
# # Question on list comprehensions in Python

# l = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]

# print("here are the positive numbers")
# # Using list comprehension to filter out negative numbers
# for i in l:
#     if i>=0:
#         print(i)
# # Output: [1, 2, 3, 4, 5]
# print("here are the negative numbers")      

# for i in l:
#     if i<0:
#         print(i)
# # Output: [-1, -2, -3, -4, -5]

# Mean of List elements

# num = [1, 2, 3, 4, 5]
# mean = sum(num) / len(num)
# print("Mean of the list is:", mean)

# sum =0
# for i in num:
#     sum += i
     
# print(sum / len(num))

# # Find the greatest element and print its index too?
# num = [23, 45, 67, 89, 12, 34, 56]
# largest = num[0]
# for i in range(len(num)):
#     if num[i] > largest:
#         largest = num[i]
#         index = i
# print(f"Greatest element is: ${largest} and Index of greatest element is: {index}")
# # Output: Greatest element is: 89
# # Output: Index of greatest element is: 3

# # Find the second greatest element?

# num = [23, 45, 67, 89, 12, 34, 666, 100]
# largest = num[0]
# second_largest = num[0]

# for i in range(len(num)):
#     if num[i] > largest:
#         second_largest = largest
#         largest = num[i]
#     elif num[i] > second_largest and num[i] != largest:
#         second_largest = num[i]
# print(f"Second greatest element is: {second_largest}")
# # Output: Second greatest element is: 67

# #  Check if List is sorted or not

# num = [1, 2, 3, 44, 5, 6]
# for i in range(len(num) - 1):
#     if num[i] > num[i + 1]:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")


# # tuple


# a = (1,2,3,4,5,6,7,7,7.6, print(), "hello" )

# for i in range(len(a)):
#     print(a[i])
    
# # set in python 

# a ={1,2,3,4}
# print(type(a))

# print(a)


# # dictionary in python

# dic = {1:"one", 2:"hello", 3:"hello"}
# for i in dic:
#     print(dic[i])

# # # Dictionary Questions
# # Write a Python script to merge two Python dictionaries?

# d1 ={10:"100",20:"20", 30:"30"}
# d2 ={40:"400",50:"500",60:"600"}

# for i in d2:
#     d1[i]= d2[i]
# print(d1)

# # Write a Python program to sum all the values in a dictionary?
# d3 ={1:10,2:20,3:30,4:4000000}
# sum = 0
# for i in d3:
#     sum = sum + d3[i]
# print((f"the sum of d3 ${sum}"))


# # Count the frequency of each element

# lis = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4]

# d ={}
# for i in lis:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# """ Write a Python program to combine two dictionary by adding
# values for common keys."""

# d1 ={10:100,20:20, 40:30}
# d2 ={40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)

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

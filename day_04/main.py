

# # For Loop questions

# # Accept an integer and Print hello world n times 

# N = int(input("Enter an integer: "))

# for i in range(N):
#     print("Hello World")

# # Print natural number up to n 
# n= int(input("Enter a natural number: "))
# for i in range(1, n + 1):
#     print(i)


# #  Reverse for loop. Print n to 1  

# ReverseNumber = int(input("Enter a natural number: "))
# for i in range(ReverseNumber,0, -1):
#     print(i)
    

# # Take a number as input and print its table 

# number = int(input("Enter a number to print its table: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


# # Sum up to n terms 
# n_turms = int(input("Enter the number of terms to sum: "))
# sum = 0
# for i in range(1, n_turms + 1):
#     sum += i
# print(f"The sum of the first {n_turms} terms is: {sum}")

# # Factorial of a number 
# n = int(input("Enter a number to calculate its factorial: "))
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
# print(f"The factorial of {n} is: {factorial}")

# Print the sum of all even & odd numbers in a range separately.

# n = int(input("Enter a natural number: "))
# sum_even = 0
# sum_odd = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
# print(f"The sum of even numbers from 1 to {n} is: {sum_even}")
# print(f"The sum of odd numbers from 1 to {n} is: {sum_odd}")
 
 
# #  Print all the factors of a number 

# n = int(input("Enter a number to find its factors: "))
# factors = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         factors.append(i)
# print(f"The factors of {n} are: {factors}")

# """ Accept a number and check if it a perfect number or not.
#  A number whose sum of factors is equal to the number itself
#  Ex - 6 = 1, 2, 3 = 6 (perfect number) """
 
# n = int(input("Enter a number to check if it's a perfect number: "))
# factors_sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         factors_sum += i
# if factors_sum == n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")

# Check wether the number is prime or not 

# n = int(input("Enter a number to check if it's prime: "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")

# Reverse a string without using in build functions.

# string = input("Enter a string to reverse: ")
# string2 = ""
# for i in range(len(string) - 1, -1, -1):
#     string2 = string2 + string[i]
    

# print(string2)

# Check string is Pallindrome or not 

# char1 = input("Enter a string to check if it's a palindrome: ")
# char2 = ""
# for i in range(len(char1) - 1, -1, -1):
#     char2 = char2 + char1[i]
# if char1 == char2:
#     print(f"{char1} is a palindrome.")
# else:
#     print(f"{char1} is not a palindrome.")



str1 = input("Enter a string to analyze: ")

# Initialize counters
chars = 0
digits = 0
symbols = 0

# Loop through each character in the string
for char in str1:
    if char.isalpha():           # Check if it's a letter
        chars += 1
    elif char.isdigit():         # Check if it's a digit
        digits += 1
    else:                        # Everything else is a symbol
        symbols += 1

# Print the results
print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)
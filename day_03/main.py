userAge = int(input(("what is you age:-")))

# if stamtement
if userAge<12:
    print("Your age is less than 12")


# if elif statement
# Q4. Accept name and age from the user. Check if the user is a 


#  valid voter or not.

voteAge = int(input("Enter your age to check voting eligibility: "))
if userAge>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# if-elif-else statement for temperature
# This program checks the temperature and prints a message based on the range it falls into

temperature = int(input("Enter the temperature in Celsius: "))

if temperature<0:
    print("It's freezing!")
elif temperature<=10:
    print("It's very cold!")
elif temperature<=20:
    print("It's cold!")
elif temperature<=30:
    print("It's warm!")
elif temperature<=40:
    print("It's hot!")
else:
    print("It's very hot!")
    


# # Some Questions on Conditional 

# #Accept two numbers and print the greatest between them
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")


# Q2. Accept the gender from the user as char and print the 

#  respective greeting message ( Ex - Good Morning Sir (on the basis of gender)

gender = input("Enter your M for Male and F for Female: ").strip().upper()

if gender == 'M':
    print("Good Morning Sir")
else:
    print("Good Morning Madam")

# Q3. Accept an integer and check whether it is an even number or odd

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")



# Q5. Accept a year and check if it a leap year or not (google to find out what year is a leap year)

year = int(input("Enter a year to check if it's a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
### Questions:

# 1. **Odd or Even**: Write a program that takes an integer as input and checks whether it is odd or even.

# 2. **Age Group**: Write a program that checks a person's age and categorizes them into a group:

#    * Child (0–12)
#    * Teen (13–19)
#    * Adult (20–64)
#    * Senior (65+)

# 3. **Leap Year Check**: Write a program that checks if a given year is a leap year. A year is a leap year if:

#    * It is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

# 4. **Greatest of Three**: Write a program that takes three numbers as input and prints the greatest one.

# 5. **Vowel or Consonant**: Write a program that checks whether a given letter is a vowel or consonant.

# 6. **Positive, Negative, or Zero**: Write a program that checks if a given number is positive, negative, or zero.

# 7. **Divisibility Check**: Write a program that checks if a given number is divisible by both 3 and 5.

# 8. **Temperature Checker**: Write a program that takes a temperature in Celsius as input and checks whether it’s too cold, normal, or too hot:

#    * Below 0°C: Too Cold
#    * 0–30°C: Normal
#    * Above 30°C: Too Hot

# 9. **Multiple of 7 and 5**: Write a program that checks if a number is a multiple of both 7 and 5.

# 10. **Grade Checker**: Write a program that takes a student's grade and prints a message:

#     * A: Excellent
#     * B: Good
#     * C: Average
#     * D: Below Average
#     * F: Fail


# Answers
# 1. **Odd or Even**: Write a program that takes an integer as input and checks whether it is odd or even.

# num = int(input("Enter a Number : "))
# if num%2 ==0 :
#     print("Number is Even")
# else:
#     print("Number is Odd")



# 2. **Age Group**: Write a program that checks a person's age and categorizes them into a group:

#    * Child (0–12)
#    * Teen (13–19)
#    * Adult (20–64)
#    * Senior (65+)


# age = int(input('Enter Your Age : '))

# if 0<=age<=12:
#     print("Child")
# elif 13<= age <=19:
#     print("Teen")
# elif 20<= age <=64:
#     print("Adult")
# elif age >=65:
#     print("Senior")
# else:
#     print("Not a Valid Number")

#3. **Leap Year Check**: Write a program that checks if a given year is a leap year. A year is a leap year if:

# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 != 0 or year % 400 == 0:
#         print(f"{year} is a Leap Year")
#     else:
#         print(f"{year} is not a Leap Year")
# else:
#     print(f"{year} is not a Leap Year")


# 4. **Greatest of Three**: Write a program that takes three numbers as input and prints the greatest one.
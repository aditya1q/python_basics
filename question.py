# 🐍🐍 append the variable in list
# fruites = []

# f1 = input('Enter fruite: ')
# fruites.append(f1)
# f2 = input('Enter fruite: ')
# fruites.append(f2)
# f3 = input('Enter fruite: ')
# fruites.append(f3)

# print(fruites)


# 🐍🐍 enter the number and sort (if you are not using int then it will append alphabatically)
# number = []

# n1 = int(input('Enter number: '))
# number.append(n1)
# n2 = int(input('Enter number: '))
# number.append(n2)
# n3 = int(input('Enter number: '))
# number.append(n3)
# number.sort()
# print(number)

# 🐍🐍 print function is prime or not using if else ladder

# num = int(input('Enter the number: '))

# if(num <=2):
#     print('this is prime number')
# elif(num % 2 == 0 ):
#     print('this is not prime')
# else:
#     print('this is prime number')

# 🐍🐍 print function is prime or not using for

# num = int(input('Enter the number: '))

# for i in range(2, num):
#     if(num % i == 0):
#         print('this is not prime')
#         break
# else:
#     print('this is prime')

# 🐍🐍 print function for sum the given number while loop

# n = int(input('Enter the number: '))
# i = 1
# sum = 0
# while(i <= n) :
#     sum += i
#     i += 1
# print(sum)

# 🐍🐍 factorial of given number for loop

# n = int(input('Enter the Number: '))

# product = 1
# for i in range (1, n + 1):
#     product = product * i
# print(product)

# 🐍🐍 1. write a star program  # enter 5 for desired output
#   *
#  ***
# *****

# n = int(input('Enter the Number: '))
# for i in range(1, n+1):
#     print(" " * (n-i) ,end="")
#     print("*" * (2*i-1), end="")
#     print('')


# 🐍🐍 2. write a star program # enter 3 for desired output
# ***
# **
# *

# n = int(input('Enter the Number: '))
# for i in range(1, n+1):
#     print("*" * (n-i+1), end="")
#     print('')


# 🐍🐍 3. write a star program  # enter 3 for desired output
# *
# **
# ***

# n = int(input('Enter the Number: ')) 

# for i in range(1, n+1):
#     print("*" * i, end="")
#     print('')

# 🐍🐍 4. write a star program  # enter 4 for desired output
# ****
# ****
# ****

# n = int(input('Enter the Number: ')) 
# for i in range(1,n+1):
#     print("*" * n, end="")
#     print('')


# 🐍🐍 5. write a star program # enter 4 for desired output
#    *
#   **
#  ***
# ****

# n = int(input('Enter the Number: '))

# for i in range(1, n+1):
#     print(" " * (n - i), end="")
#     print("*" * i, end="")
#     print('')

# 🐍🐍 6. write a star program # enter 4 for desired output
# ****
#  ***
#   **
#    *

# n = int(input('Enter the Number: '))

# for i in range(1, n + 1):
#     print(" " * i, end="")
#     print("*" * (n - i + 1), end="")
#     print('')

# 🐍🐍 7. write a star program # enter 4 for desired output

#    A
#   BBB
#  CCCCC
# DDDDDDD

# n = int(input('Enter the Number: '))
# alph= 65

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print(chr(alph) * (2*i - 1), end="")
#     alph += 1
#     print('')

# 🐍🐍 8. write a star program # enter 4 for desired output

#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E 

# n = int(input("Enter the Number: "))

# for i in range(n):  # Rows
#     print(" " * (n - i - 1), end="")  # Leading spaces

#     for j in range(i + 1):  # Print letters A, B, C, ...
#         print(chr(65 + j), end=" ")  

#     print()  # Move to the next line


# 🐍🐍 9. write a star program # enter 4 for desired output

#     1
#    123
#   12345
#  1234567
# 123456789

n = int(input('Enter the Number: '))

for i in range(n, 0, -1):
    print("*" * (n - i - 1), end="")

    # for j in range(i + 1):
    #     print((j + 1), end="")
    print('')
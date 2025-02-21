# 🐍🐍🐍🐍 if elif else ladder : 

# age = int(input("Enter your age: "))
# if(age >= 18):
#     print("you can drive")
# elif(age < 0):
#     print("you are not born yet")
# else :
#     print("you can not drive")


# 🐍🐍🐍🐍 for loop

# print the table of 2

# n=2
# for i in range(1, 11):
#     print(f'{n} * {i} = {n * i}')

# print the number : from 2 to 49
# for i in range(1, 50):
#     print(i)

# for loop applied on list and set also

# a = ["aadi", "kanha", "ashu", "aisha"]

# for name in a:  # Loop through each item
#     print(name)

# if "aadi" in a: # for particular element
#     print("yes present in the list")
# else:
#     print("invailid name")


# 🐍🐍🐍🐍 while loop: make sure to false while loop condition otherwise it will cause infinite loop

# i = 0  # Initialize i with 0

# while(i <= 7):  # Loop runs while i is less than or equal to 7
#     print(i)  # Print current value of i
#     i += 1  # Increment i by 1 in each iteration, otherwise above print run forever becuase i is not incresing (infinite loop)

# print("end")  # This runs after the loop ends


# 🐍🐍🐍🐍 continue statement : it will escape the current iteration and move to next one

# i = 0
# while(i <= 50):
#     if i == 45:
#         i += 1  # Increment BEFORE continue
#         continue  # Skip printing 45
    
#     print(i)
#     i += 1  # Regular increment

# print('end')

#  🐍🐍🐍🐍 break stement : it will jump out of the loop

# i = 0
# while(i <= 5):
#     if(i==4) :
#         i += 1 # runs before break
#         break # jump out of the loop and not check the other upcoming conditions
#     print(i)
#     i += 1
# print('end')

# pass statement : sometimes we want to pass or stop the previous thing or code then we can use that statement

# this statement passed successfully 
# for i in range(3):
#     pass

# # directly this statement runs
# n = int(input('Enter the Number: '))
# for i in range(1,11):
#     print(f'{n} * {i} = {n * i}')

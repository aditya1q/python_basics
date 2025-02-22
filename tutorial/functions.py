# 🐍🐍 factorial of number: 

# def factorical(n):
#     if(n <= 1): return 1
#     return n * factorical(n - 1)

# num = int(input('Enter the Number: '))
# print(factorical(num))


# 🐍🐍 f_to_C to f: 

# def f_to_C(f):
#    n = (5/9) * (f - 32)
#    return round(n , 2)
# a = f_to_C(100)
# print(a)


# 🐍🐍 sum of n number without recursive: 
# def sum(n):
#     if(n <=1): return 1
#     return (n * (n + 1))/2
# num = int(input("Enter the Number: "))
# total = sum(num)
# print(f'Sum of Number is {int(total)}')


# 🐍🐍 sum of n number with recursive: 
# def sum_recursive(n):
#     if(n <= 1): return 1
#     return n + sum_recursive(n - 1)
# num = int(input("Enter the Number: "))
# total = sum_recursive(num)
# print(f'Sum of numbers {num} is {int(total)}')


# 🐍🐍 pattern-1 using recursion: 

# def recursion_pattern(n):
#     if(n == 0): return
#     print("*" * n)
#     recursion_pattern(n-1)
# num = int(input("Enter the Number: "))
# pattern = recursion_pattern(num)


# 🐍🐍 pattern-2 using recursion: 

# def recursion_pattern(n, i=1):
#     if(n <= i): return
#     print(" " * (n - i) + "*" * i)  # Print spaces and stars
#     recursion_pattern(n, i + 1) 
# num = int(input("Enter the Number: "))
# pattern = recursion_pattern(num)


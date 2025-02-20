# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)

# a = int(input('Enter number 1 :'))
# b = int(input('Enter number 2 :'))
# c = a + b
# print(c)


# a=5 
# b=5
# print(a+b)


# a = int(input('Enter Number: '))
# b = a % 2 == 0
# print(b)


# a = int(input('Enter Number 1: '))
# print(a * a)


# a = int(input('Enter Number 1: '))
# b = int(input('Enter Number 2: '))
# print(int((a+b)/2))


#🐍🐍🐍🐍 String Methods :::: strings are imutable in python so we can not change the value of variable if we assigned string in that variable 
# name = 'aditya'
# print(len(name)) # get the length of name variable (length starts from one and index starts from 0)
# print(name.endswith('ya')) # return true or false
# print(name.startswith('ad')) # return true or false
# print(name.capitalize()) # make the first letter capital only
# print(name.islower()) # make it lower case
# print(name.find('t')) # if t present retun index number of that 


#🐍🐍🐍🐍 strings are imutable means we can not change the original string it will return new string if i cahnge the variable
# name = 'aadi'
# print(name)
# newname = name.replace('aadi', 'kanha')
# print(newname)


#🐍🐍🐍🐍 list are mutable means we can change the original list 
# arr = [2,3,5,6,4]
# arr.append(33) # add number in last
# print(arr)
# arr.insert(2, 3333) # insert the number in index 2
# print(arr )
# arr.remove(4) # remove the number if present in list otherwise return -1
# print(arr)


#🐍🐍🐍🐍 tuple example: tuple are immutable
# arr = (1,2,3,4,5,6,3,4,4,4,4,)
# print(type(arr))
# count the given number in my tuple
# getcount = arr.count(4) # count the given number in tuple
# print(getcount)
# getindex = arr.index(5) # if the number is present in tuple then it's only give the first index number in my tuple
# print(getindex)

#🐍🐍🐍🐍 concate tuple: tuple are imutable so we can't change the tuple it's always return new tuple
# arr1 = (1,2,3,4)
# arr2 = (5,6,7,8)
# newtuple = arr1 + arr2 # concat the tuple
# print(newtuple)

#🐍🐍🐍🐍 unpacking(in js destructuring) tuple
# arr1 = (1,2,3)
# a,b,c = arr1 # now it's store individual values in these variable
# print(a,b,c)


#🐍🐍🐍🐍 dictionry(like object in js):
# dictinary are unorderd
# can't update duplicate keys
# it is indexed 
# Since dictionaries are mutable, 
# the change happens in-place, meaning the original dictionary is updated.. 

# arr = {
#     "name": "aadi",
#     'rank': 3,
#     "course": 'MCA'
# }
# changename = arr['name'] = 'kanha'
# arr.update({"name":"kanha"})
# print(arr['name'])
# print(changename)
# arr.keys()
# arr.values()
# print(arr)

#🐍🐍🐍🐍 some dictionary methods: 
d = {"name": "Alice", "age": 25, "city": "NY"}

# print(d.get("name"))        # Alice
# print(d.keys())             # dict_keys(['name', 'age', 'city'])
# print(d.values())           # dict_values(['Alice', 25, 'NY'])
# print(d.items())            # dict_items([('name', 'Alice'), ('age', 25), ('city', 'NY')])

# d.update({"country": "USA"})
# print(d)                    # {'name': 'Alice', 'age': 25, 'city': 'NY', 'country': 'USA'}

# d.pop("age")
# print(d)                    # {'name': 'Alice', 'city': 'NY', 'country': 'USA'}

# d.setdefault("gender", "Female")
# print(d)                    # {'name': 'Alice', 'city': 'NY', 'country': 'USA', 'gender': 'Female'}

# d.popitem()
# print(d)


#🐍🐍🐍🐍 copy dictionary: This modifies the original dictionary (arr), not a new one. If you want a new dictionary, you can use .copy() like this:
# new_arr = arr.copy()
# new_arr['name'] = 'kanha'


#🐍🐍🐍🐍 set: set are immutable and contain unique values (means if you write two duplicate value in set then it will eliminate the duplicate vlaue and showing value once)
# arr = [1,2,3,4,5,3,2,4] # this is list
# getvalue = set(arr)
# print(getvalue)
# print(getvalue)
# print(type(getvalue))

# arr = {1,2,3,4} # this is set
# print(type(arr))
# arr =  set() # you can create emty set like this
# print(type(arr))
# arr =  {1,} # or you can create emty set like this
# print(type(arr))

# 🎯 Why Use Hashing?
# ✅ Fast Searching → Find data in O(1) time instead of O(n).
# ✅ Avoid Duplicates → Sets use hashing to store unique values.
# ✅ Efficient Memory Usage → No need to store data in order.

# 🎯 Hashing is a way to convert data into a unique number (called a hash) so it can be quickly found later.

# Think of it like storing books in a library:
# Each book has a unique ID (hash).
# When you search for a book, you don’t check every shelf—you go straight to the correct section using the ID.
# This makes searching super fast instead of checking every book one by one.

# 🐍🐍🐍🐍 set methods: sets are unordered

# arr = {1,2,3,4,5,6,7}
# arr.add(7) # add number in set
# print(arr)
# print(len(arr)) # return the length of an arr

# arr.remove(6) # remove number in set if exists and if not, raise error
# print(arr)
# arr.discard(6) # remove number in set if exists and if not, not raise error
# print(arr)

# arr.pop() # delete random element in set and we can not use popItem
# print(arr)

# arr.clear() # clear the set
# print(arr)

# arr.union({8,9}) # return new set with all items of both sets
# print(arr)

# arr.intersection({4,8}) # return new set which containes only items in both sets {4}
# print(arr)


# arr1 = {1,2,3,4}
# arr2 = {1,2,3,4,5,6,7,8}
# print(arr1.issubset(arr2)) # Returns True if arr1 is a subset of arr2 (means arr1 element are present in arr2)
# print(arr1.issuperset(arr2)) # Returns False if arr1 contains all elements of arr2 (means all arr1 element present in arr2)
# print(arr1.isdisjoint(arr2)) # Returns False if s1 and s2 have no common elements  (means if no element of arr1 is present in arr2)
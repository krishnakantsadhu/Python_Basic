bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

for bicycle in bicycles:
    print(bicycle)

ind = [i for i, bicycle in enumerate(bicycles) if(bicycle == 'redlinew')]

print(ind)

"""
Method          	Description
------              ---------------------------------
append(x)	        Adds an element x to the end of the list
extend(iterable)	Adds all elements from an iterable (like another list)
insert(i, x)	    Inserts x at position i
remove(x)	        Removes the first occurrence of x
pop([i])	        Removes and returns the element at index i (default: last)
clear()	            Removes all items from the list
index(x)	        Returns the index of the first occurrence of x
count(x)	        Returns the number of times x appears
sort()	            Sorts the list in-place (can take key= and reverse= args)
reverse()	        Reverses the list in-place
copy()	            Returns a shallow copy of the list
"""

fruits = ['apple', 'banana', 'cherry']

fruits.append('date')       # ['apple', 'banana', 'cherry', 'date']
print("1. "+str(fruits))

fruits.insert(1, 'kiwi')     # ['apple', 'kiwi', 'banana', 'cherry', 'date']
print("2. "+ str(fruits))

fruits.remove('banana')# ['apple', 'kiwi', 'cherry', 'date']
print("3. "+ str(fruits))

fruits.pop()                 # Removes 'date'
print("4. "+str(fruits))

print(fruits.index('cherry'))  # 2

print(fruits.count('apple'))   # 1

fruits.sort()                 # ['apple', 'cherry', 'kiwi']
print("8. "+ str(fruits))

fruits.reverse()              # ['kiwi', 'cherry', 'apple']
print("9. "+ str(fruits))

copy_list = fruits.copy()
print("1. "+str(copy_list))
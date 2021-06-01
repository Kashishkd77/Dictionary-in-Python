# DICTIONARY Built-in Functions illustration :

dic={1:'a',3:'b',2:'c',4:'d'}
print("DICTIONARY Built-in Functions illustration :")
#len(object) function --> returns the total count of elements in a dictionary
print("1. Length of dictionary is : ",len(dic))

#sorted(object) function --> Return a new sorted dictionary in ascending order by default
sorted(dic)
print("2. Sorted order of dictionary is : ",dic)

#all(object) function --> Return true if all keys of the dictionary are True
all(dic)
print("3. Using all() built in function is : ",dic)

#any(object) function --> Return true if any keys of the dictionary are True
any(dic)
print("4. Using any() built in function is : ",dic)
print()
print()

# DICTIONARY Method Functions illustration :
print("DICTIONARY Method Functions illustration : ")

#copy()	: Returns a shallow copy of the dictionary.
print("1. copy() method : ")
dic1=dic.copy()
print("Assigning one dictionary to another using copy() : ",dic1)
print()

#update([other]) : Updates the dictionary with the key/value pairs from other, overwriting existing keys.
print("2. update() method : ")
d2={2:'xyz'}
dic.update(d2)
print("Updating an element using update() : ",dic)
d2={5:'mno'}
dic.update(d2)
print("Updating dictionary by adding an element using update() : ",dic)
print()

#pop(key[,d]) : Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
print("3. pop() method : ")
dic.pop(1)
print("Deleting an element of given key value using pop() : ",dic)
print()

#popitem() : Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
print("4. popitem() method : ")
dic.popitem()
print("Deleting an arbitrary element using popitem() : ",dic)
print()

#clear() : Removes all elements from the set
print("5. clear() method : ")
dic.clear()
print("Deleting all elements using clear() : ",dic)
print()

#OTHER METHODS OF DICTIONARY :
#fromkeys(seq[, v])	: Returns a new dictionary with keys from seq and value equal to v (defaults to None).
#get(key[,d]) : Returns the value of the key. If the key does not exist, returns d (defaults to None).
#keys()	: Returns a new object of the dictionary's keys.
#setdefault(key[,d]) : Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).
#items() : Return a new object of the dictionary's items in (key, value) format.
#values() : Returns a new object of the dictionary's values

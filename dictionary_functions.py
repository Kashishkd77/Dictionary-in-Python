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
print("Item popped : ",dic.pop(1))
print("Deleting an element of given key value using pop() : ",dic)
print()

#popitem() : Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
print("4. popitem() method : ")
print("Item popped : ",dic.popitem())
print("Deleting an arbitrary element using popitem() : ",dic)
print()

#clear() : Removes all elements from the set
print("5. clear() method : ")
dic.clear()
print("Deleting all elements using clear() : ",dic)
print()

#fromkeys(seq[, v])	: Returns a new dictionary with keys from seq and value equal to v (defaults to None).
print("6. fromkeys(seq[,v]) method : ")
keys={2,3,5,7}
value='prime number'
dict3=dict.fromkeys(keys,value)
print("Creating new dictionary dict3 using fromkeys() : ",dict3)
print()

#get(key[,d]) : Returns the value of the key. If the key does not exist, returns d (defaults to None).
print("7. get(key[,d]) method : ")
print("Accessing element of key=3 in dict3 using get() : ",dict3.get(3))
print()

#keys()	: Returns a new object of the dictionary's keys.
print("8. keys() method : ")
print("All the keys in dict3 using keys() : ",dict3.keys())
print()

#setdefault(key[,d]) : Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).
print("9. setdefault(key[,d]) method : ")
dict1={1:'a',2:'b',3:'c'}
d1=dict1.setdefault(3)
d2=dict3.setdefault(4,None)             #Key=4 will be inserted in dict3
print("Setting default key in dict1 using single argument of setdefault() : ",dict1)
print("Setting default key in dict3 using both argument of setdefault() : ",dict3)
print()

#items() : Return a new object of the dictionary's items in (key, value) format.
print("10. items() method : ")
print("All elements in dict3 using items() : ",dict3.items())
print()

#values() : Returns a new object of the dictionary's values
print("11. values() method : ")
print("Values of all elements in dict1 using values() : ",dict1.values())
print()

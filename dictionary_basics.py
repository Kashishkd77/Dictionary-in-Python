# DICTIONARY Basics : ordered , unindexed , mutable and no duplicate values allowed
# DICTIONARY can contain mutable elements like lists,sets,dictionaries,etc.

#CREATION -->
# METHOD 1 : with {} has key and corresponding value
empty_dic={}
single_dic={ 1 : 'a', 2 : 'b' , 3 : 'c' }                       #dictionary with integer keys
# METHOD 2 : Using built-in function "dict()"
mixed_dic=dict({ 1 : 'a', 'name' : 'kashish' ,  4.1 : 5.6 })
#Nested Set is not allowed
nested_dic=dict({ 1 : 'a', 'name' : 'kashish' , 3.9 : ['c',6.78,9] , 4.1 : 5.6 , 2 : single_dic, 'm' : empty_dic})
print("CREATING SET : ",nested_dic)
print()

#type() method
print("TYPE OF BUILT IN DATA TYPE : ",type(single_dic))       #type() : Returns the type of data type
print()

#ACCESSING ELEMENTS OF DICTIONARY :
#METHOD 1 : Using keyvalue (doesnt use indexing)
print("ACCESSING ELEMENTS OF DICTIONARY : ")
print("1.1 . First element of nested_dic : ",nested_dic[1])
print("1.2 . Accessing an element from another element of nested_dic : ",nested_dic[3.9][1])
#Empty dictionary cannot have indexing i.e. nested_dic['m'][0] not possible
print("1.3 . Sixth element of nested_dic i.e. Empty dictionary : ",nested_dic['m'])
#METHOD 2 : Using get() method
print("2 . Accessing element using get() : ",nested_dic.get(4.1))
print()

#CHANGING IN DICTIONARY :
print("CHANGING IN DICTINARY : ")
#METHOD 1 : Adding an element
single_dic[4]='c'
print("1 . Adding an element in dictionary : ",single_dic)
#METHOD 2 : Updating elements
single_dic[1]='ab'
print("2. Updating elements in dictinary : ",single_dic)
print()

#SPECIAL FEATURES OF DICTIONARY or DICTIONARY COMPREHENSIONS :
print("SPECIAL FEATURES OF DICTIONARY :")
# 1 . Use of for statement within list brackets
print("1. Use of 'for' statement within dictionary brackets : ")
power={ x: 2 ** x for x in range(5) }          #prints square of 0 to 4
print(power)
#1 Another way :
#power={}
#for x in range(5):
    #power[x]=2**x
#print(power)

# 2 . Use of for and if statement within list brackets
power1={ x : x * x for x in range(10) if x>5}                   #the entire dictionary gets stored in power1
print("2 . Use of 'for' and 'if' statement within dictionary brackets : ",power1)
print()


#DELETING IN DICTI0NARY :
print("DELETING IN DICTIONARY :")
#METHOD 1 : Using pop() method : Removes and returns an element
single_dic.pop(1)
print("1. Deleting an element with key value '1' using pop() : ",single_dic)

#METHOD 2 : Using popitem() method : Removes arbitrary element and returns its (key,value)
single_dic.popitem()
print("2. Deleting an arbitrary element using popitem() : ",single_dic)

#METHOD 3 : Using clear() method : Removes all elements of list
mixed_dic.clear()
print("3. Deleting all elements using clear() : ",mixed_dic)

#METHOD 4 : Using del : Deletes entire dictionary
del empty_dic
print("4. Deleting entire dictionary using del : ")
#print("4. Deleting entire dictionary using del : ",empty_dic)          --> throws NameError

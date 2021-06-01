# DICTIONARY Operations illustration : (only 2 operations are in list)

dic=dict({ 1 : 'a', 'name' : 'kashish' , 3.9 : ['c',6.78,9] , 4.1 : 5.6 })

#OPERATION 1 -> Using "in" and "not in" keyword : Returns True/False
print("OPERATION 1 : Using 'in' and 'not in' keyword")
#"in" keyword --> Key value is considered
print("Is 'Kashish' present in list? : ",'Kashish' in dic)
print("Is 'name' present in list? : ",'name' in dic)
#"not in" keyword
print("Is 'Kashish' not present in list? : ",'Kashish' not in dic)
print("Is 'True' not present in list? : ",True not in dic)
print()

#OPERATION 2 -> Iterating through a dictionary
print("OPERATION 2 : Iterating through a dictionary using for loop")
#accessing the elements of dictionary by value and not index , using for loop to iterate through list
print("Example 1 : ")
for i in dic:
    print(dic[i])               #value gets printed , not key
print("Example 2 : ")
for i in {1:7,2:89,3:'d'}:
    print(i)                    #key gets printed , not value
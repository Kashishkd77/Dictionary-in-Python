#DICTIONARY PROBLEM :
#WHEN YOUR SAME CONTACT HAS TWO OR MORE PHONE NUMBERS --> use list,set,tuple,etc
contact={ 'kashish' : [8842101111,9115000009] ,
          'ayushi': {809242101,9110000509},
          'sangeet' : (882348791,9111152709) ,
          'palak' : { 1 : 9042222101, 2 : 9115052209 }
        }
print("First number of 'KASHISH' : ",contact['kashish'][0])
print("Numbers of 'AYUSHI' : ",contact['ayushi'])
print("Second number of 'SANGEET' : ",contact['sangeet'][1])
print("First number of 'PALAK' : ",contact['palak'][1])            #number at keyvalue=1


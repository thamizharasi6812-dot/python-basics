#set{} 
a={1,2,3,4}
b={1,2,5,6}
a.union(b)                    #combines both the set without duplicates
a.add(5)                      # add the element to the set
a.copy()                      #copy the set
a.difference(b)               #returns the differnce between the sets
a.symmetric_difference(b)     #returns both differnce of the set
a.difference_update(b)        #returns the differnce as the set
a.symmetric_difference_update(b) #returns both differnce as set
a.intersection(b)             #returns the common values of the set
a.intersection_update(b)      #updates the common value of the set       
a.isdisjoint(b)               #returns true if the set are not connected
a.issubset(b)                 #returns true if the set b contains all elements of set a
a.issuperset(b)               #returns true if set a contains all elements of set b
a.discard(2)                  #remove the particular element from the set
a.pop()                       #returns random element from the set
a.remove(3)                   #removes the particular element
a.clear()                     #clear the set 

#dict={}
a={'name':'alice','exam.no':363728,'center':'ooty'}
a.get('name')                 #returns the value of particular key
a.items()                     #returns the items as seperate tuple inside a list
a.keys()                      #returns the keys as list
a.pop('exam.no')              #returns the particular value of the key
a.popitem()                   #returns the remaining iteams of the dict{}
a.setdefault('name')          #returns the default value if it is not found in dict{}
a.update()                    #updates the dict{}
a.values()                    #returns the values of the dict{}
a.copy()                      # copy the iteams
a.clear()                     #clear the dict{}
dir({})
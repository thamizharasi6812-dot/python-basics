#exercise-1
text="hello hello world!"
a=text.split()
# a=list(set(text.split()))
dict_1={}
dict_1[a[0]]=a.count(a[0])
dict_1[a[1]]=a.count(a[1])
dict_1[a[2]]=a.count(a[2])

#exercise-2
dict_2={'Dheekshan':6381473733,
        'Poojha' :8766073745,
        'Prakash':7765322099,
        'Ram':9908765133,
        'Thamizh':9347857814, 
        'Thendral':7549062568}
dict_2.update({'lavanya':7443889898})    #added new item in the dict{}
dict_2.get('Thamizh')                    #returns the value of the key
dict_2.pop('Ram')                        #removes the iteam from the dict{}

#exercise-3
a=[10,20,30,40,50]
b=[10,20,30,60,70]
c=list(set(a) ^ set(b))                  #the value in the c list is symmetric differnce between a and b list
print(c)
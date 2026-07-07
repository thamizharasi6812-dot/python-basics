#basic comprehenion
cube={x:x**3 for x in range(1,6)}
#dictionary comprehenion with if 
number={x:'even'for x in range(1,10) if x%2==0}
#dictionary comprehension with if else
number={x:'even' if x%2==1 else 'odd' for x in range(1,11)}

# set comprehension
# basic comprehension
set={x for x in range(1,51)}
# set comprehension with if 
a={'apple','banana','cherry','durian'}
fruits={a for a in a if len(a)>4}
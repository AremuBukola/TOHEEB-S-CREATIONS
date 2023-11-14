#!/usr/bin/env python
# coding: utf-8

# ### MULTIPLICATION

# In[1]:


# Python3 program to multiply all values in the
# list using math.prod
 
import math
list1 = [2, 3, 6] 
result1 = math.prod(list1)
print(result1)


# ### SORTING LIST

# In[2]:


def last(n):
    return n[-1]  
  
def sort(tuples):
    return sorted(tuples, key=last)
  
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted:")
print(sort(a))


# ### ADDING DICTIONARIES

# In[4]:


# initializing dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
 
# calculating resultant dictionary
c = {i: d1.get(i, 0) + d2.get(i, 0) 
     for i in set(d1).union(d2)}
 
# printing result
print(c)


# ### INTEGRAL

# In[17]:


def numberDict(n):
    numberDict = {}
    for i in range(1, n+1):
        numberDict[i] = i*i
    print(numberDict)


# In[18]:


numberDict(8)


# ### SORTING TUPLE FLOAT

# In[22]:


def Sort(tup):  
    return(sorted(tup, key = lambda x: float(x[1]), reverse = True))  
tup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'),] 
print(Sort(tup))


# In[23]:


set1 = set([0, 1, 2, 3, 4,])
print("\nSet with the use of Numbers: ")
print(set1)


# ### ITERATION OVER SET

# In[26]:


# Creating a set using string
test_set = set("AREMU")
 
# Iterating using for loop
for val in test_set:
    print(val)


# ### ADDING ITEM IN A SET 

# In[28]:


# set of letters
OLA = {6, 2, 3, 4}
 
OLA.add(1)
print('Letters are:', OLA)
 


# ### REMOVE ITEM FROM SET

# In[34]:


OLA = set([12, 10, 13, 15, 8, 9])
 
for i in range(len(OLA)):
    OLA.remove(next(iter(OLA)))
    print(OLA)


# In[ ]:





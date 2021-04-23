#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Method - append() --- Adds an element at the end of the list

names = ["Jim", "John", "Joey"]
names.append("Jason")
print(names)


# In[2]:


# Method - clear() --- Removes all the elements from the list

names = ["Jim", "John", "Joey"]
names.clear()
print(names)


# In[3]:


# Method - copy() --- Returns a copy of the list

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)


# In[4]:


# Method - count() --- Returns the number of elements 
# with the specified value 

names = ["Jim", "John", "Joey"]
x = names.count("Joey")
print(x)


# In[5]:


names = ["Jim", "John", "Joey", "Bruno", "Bruno"]
x = names.count("Bruno")
print(x)


# In[6]:


# Method - extend() --- Add the elements of a list (or any iterable), 
# to the end of the current list

names = ["Jim", "John", "Joey"]
nums = [1, 2, 3]
names.extend(nums)
print(names)


# In[7]:


# Method - index() --- Returns the index of the first element 
# with the specified value

names = ["Jim", "John", "Joey"]
x = names.index("Joey")
print(x)


# In[8]:


names = ["Jim", "John", "Joey"]
x = names.index("Jim")
print(x)


# In[9]:


# Method - insert() --- Adds an element at the specified position

names = ["Jim", "John", "Joey"]
names.insert(2, "Jack")
print(names)


# In[10]:


# Method - pop() --- Removes the element at the specified position

names = ["Jim", "John", "Joey"]
names.pop(-1)
print(names)


# In[11]:


# Method - remove() --- Removes the first item with the specified value

names = ["Jim", "John", "Joey"]
names.remove("Joey")
print(names)


# In[12]:


names = ["Jim", "John", "Joey"]
names.remove("Jim")
print(names)


# In[13]:


# Method - reverse() --- Reverses the order of the list

names = ["Jim", "John", "Joey"]
names.reverse()
print(names)


# In[14]:


# Method - sort() --- Sorts the list 

names = ["Jim", "John", "Joey"]
names.sort()
print(names)


# In[17]:


names = ["Alexandre", "Bruno", "Jacob", "Yossef", "Abraham"]
names.sort()
print(names)


# In[18]:


names = ["Alexandre, Bruno, Jacob, Yossef, Abraham"]
names.sort()
print(names)


# In[ ]:





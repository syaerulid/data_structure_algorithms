#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bubble_sort(elements):
    size = len(elements)
    
    for i in range(size-1):
        if elements[i] > elements[i+1]:
            tmp = elements[i]
            elements[i] = elements[i+1]
            elements[i+1] = tmp


# In[2]:


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,24]
    
    bubble_sort(elements)
    print(elements)


# In[10]:


def bubble_sort(elements):
    size = len(elements)
    
    for k in range(2):
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp


# In[11]:


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,24]
    
    bubble_sort(elements)
    print(elements)


# In[8]:


def bubble_sort(elements):
    size = len(elements)
    
    for k in range(size-1):
        for i in range(size-1):
            if elements[i] > elements[i+1]: # if elements i > i+1, swap them
                tmp = elements[i] # store that element at tmp temporarely
                elements[i] = elements[i+1] # replace element i with element i+1
                elements[i+1] = tmp # replace element i+1 with the temporarily stored (elements i that > i+1)


# In[9]:


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,24]
    
    bubble_sort(elements)
    print(elements)


# In[18]:


def bubble_sort(elements):
    size = len(elements)
    
    for i in range(size-1):
        for j in range(size-1-i): # minimizing the time, with elements already sorted not checked anymore
            if elements[j] > elements[j+1]: # if elements j > j+1, swap them
                tmp = elements[j] # store that element at tmp temporarely
                elements[j] = elements[j+1] # replace element j with element j+1
                elements[j+1] = tmp # replace element j+1 with the temporarily stored (elements i that > i+1)


# In[19]:


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,24]
    
    bubble_sort(elements)
    print(elements)


# In[20]:


def bubble_sort(elements):
    size = len(elements)
    swapped = False
    for i in range(size-1):
        for j in range(size-1-i): # minimizing the time, with elements already sorted not checked anymore
            if elements[j] > elements[j+1]: # if elements j > j+1, swap them
                tmp = elements[j] # store that element at tmp temporarely
                elements[j] = elements[j+1] # replace element j with element j+1
                elements[j+1] = tmp # replace element j+1 with the temporarily stored (elements i that > i+1)
                swapped = True
        if not swapped:
            break


# In[23]:


if __name__ == '__main__':
    elements = ['aamiir','zakiya','dini','chandra']
    
    bubble_sort(elements)
    print(elements)


# In[ ]:





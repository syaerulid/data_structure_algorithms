#!/usr/bin/env python
# coding: utf-8

# In[3]:


def insertion_sort(elements):
    """defines a function called instertion sort that have params elements"""
    for i in range(1, len(elements)):
        """this for loops iterates through the elements in the list, 
        starting from second element(index 1, because we assume that index 0 is sorted element)"""
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]: 
            """j >= 0 ensuring that we don't go out of bounds"""
            elements[j+1] = elements[j]
            """if conditions are met(shift element in sorted to the right, to make space for anchor)"""
            j = j - 1
            """decrement to check the next element in sorted region"""
        elements[j+1] = anchor


# In[4]:


if __name__== '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)


# In[ ]:





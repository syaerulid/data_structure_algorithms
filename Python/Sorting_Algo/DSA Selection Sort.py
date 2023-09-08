#!/usr/bin/env python
# coding: utf-8

# In[3]:


def selection_sort(arr):
    size = len(arr)  # Get the length of the input list 'arr'
    
    # Iterate through the list from the beginning to the second-to-last element.
    # This loop selects the minimum element in the unsorted portion of the list and moves it to its correct position.
    for i in range(size - 1):
        min_index = i  # Assume the current index 'i' has the minimum value initially.
        
        # Iterate through the unsorted portion of the list to find the minimum element.
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j  # Update 'min_index' if a smaller element is found.
                
        # Swap the element at the current index 'i' with the minimum element found.
        # This places the minimum element in its correct position.
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


# In[4]:


if __name__ == '__main__':
    elements = [78,12,15,8,61,53,23,27]
    selection_sort(elements)
    print(elements)


# In[ ]:





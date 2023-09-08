#!/usr/bin/env python
# coding: utf-8

# In[6]:


def merge_two_sorted_lists(a, b):
    sorted_list = []  # Initialize an empty list to store the merged sorted list
    len_a = len(a)    # Get the length of the first list 'a'
    len_b = len(b)    # Get the length of the second list 'b'
    i = j = 0         # Initialize two pointers 'i' and 'j' to 0

    # This loop will execute as long as both 'i' and 'j' are within the bounds of their respective lists.
    while i < len_a and j < len_b:
        # Compare the elements at the current positions 'i' in list 'a' and 'j' in list 'b'
        if a[i] <= b[j]:
            # If the element in 'a' is smaller or equal, add it to the sorted list and move the 'i' pointer forward.
            sorted_list.append(a[i])
            i += 1
        else:
            # If the element in 'b' is smaller, add it to the sorted list and move the 'j' pointer forward.
            sorted_list.append(b[j])
            j += 1

    # After the above loop, one of the lists (either 'a' or 'b') may still have some elements remaining.
    # The following two loops add any remaining elements from 'a' and 'b' to the sorted list.
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list  # Return the merged and sorted list


# In[7]:


if __name__ == '__main__':
    a = [5,8,12,56]
    b = [7,9,45,51]
    
    print(merge_two_sorted_lists(a,b))


# In[17]:


def merge_sort(arr):
    # Base case: If the input list has 1 or fewer elements, it's already sorted.
    if len(arr) <= 1:
        return (arr)

    # Calculate the midpoint of the input list.
    mid = len(arr) // 2

    # Split the input list into two halves, 'left' and 'right'.
    left = arr[:mid]
    right = arr[mid:]

    # Recursively call merge_sort on the 'left' and 'right' sublists.
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted 'left' and 'right' sublists using the merge_two_sorted_lists function.
    return merge_two_sorted_lists(left, right)


# In[18]:


if __name__ == '__main__':
    arr = [100,4,76,22,102,30,15,75]
    
    print(merge_sort(arr))


# In[39]:


def merge_sort_inplace(arr):
    # Base case: If the input list has 1 or fewer elements, it's already sorted.
    if len(arr) <= 1:
        return

    # Calculate the midpoint of the input list.
    mid = len(arr) // 2

    # Split the input list into two halves, 'left' and 'right'.
    left = arr[:mid]
    right = arr[mid:]

    # Recursively call merge_sort_inplace on the 'left' and 'right' sublists.
    merge_sort_inplace(left)
    merge_sort_inplace(right)

    # Merge the sorted 'left' and 'right' sublists using the merge_two_sorted_lists function.
    merge_two_sorted_lists(left, right, arr)  # Pass 'arr' as an argument


# In[40]:


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)    # Get the length of the first list 'a'
    len_b = len(b)    # Get the length of the second list 'b'
    i = j = k = 0     # Initialize three pointers: 'i' for 'a', 'j' for 'b', and 'k' for the index in 'a'

    # This loop will execute as long as both 'i' and 'j' are within the bounds of their respective lists.
    while i < len_a and j < len_b:
        # Compare the elements at the current positions 'i' in list 'a' and 'j' in list 'b'
        if a[i] <= b[j]:
            arr[k] = a[i]  # If 'a[i]' is smaller or equal, replace the element at 'arr[k]' with 'a[i]'
            i += 1
        else:
            arr[k] = b[j]  # If 'b[j]' is smaller, replace the element at 'arr[k]' with 'b[j]'
            j += 1
        k += 1  # Move the 'k' pointer in 'arr'

    # The following two loops add any remaining elements from 'a' and 'b' to 'arr'.
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


# In[41]:


if __name__ == '__main__':
    arr = [88,4,76,22,21,30,15,75]
    
    merge_sort_inplace(arr)
    print(arr)


# In[ ]:





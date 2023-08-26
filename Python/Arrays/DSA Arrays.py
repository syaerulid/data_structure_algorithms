#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""


# In[1]:


expense = [2200,2350,2600,2130,2190]


# In[2]:


feb_compare = expense[1] - expense[0]
print(feb_compare)


# In[6]:


first_q1 = expense[0] + expense[1] + expense[2]


# In[7]:


print(first_q1)


# In[8]:


for exp in expense:
    if exp == 2800:
        print("Yes I spend 2800$")
    else:
        print("No I am not spend 2800$")


# In[9]:


expense.append(1980)


# In[10]:


expense


# In[13]:


expense[3] = expense[3] - 200


# In[14]:


expense


# # Soal ke 2

# In[ ]:


"""
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""


# In[15]:


heros = ['spider man','thor','hulk','iron man','captain america']


# In[16]:


length_heros = len(heros)
print(length_heros)


# In[17]:


heros.append('black_panther')


# In[18]:


heros


# In[19]:


heros.remove('black_panther')


# In[22]:


heros.insert(3, 'black panther')


# In[23]:


heros


# In[26]:


heros[1:3] = ['doctor strange','doctor strange']


# In[27]:


heros


# In[29]:


heros.sort()


# In[30]:


heros


# # Soal ke-3

# In[ ]:


"""Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function"""


# In[35]:


max_num = int(input("Enter max number:"))

odd_numbers = []

for i in range(1, max_num):
    if i % 2 != 0:
        odd_numbers.append(i)
        
print("Odd numbers:", odd_numbers)


# In[ ]:





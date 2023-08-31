#!/usr/bin/env python
# coding: utf-8

# In[1]:


wmt_stock_price_queue = []


# In[2]:


wmt_stock_price_queue.insert(0, 131.10)
wmt_stock_price_queue.insert(0, 132.3)
wmt_stock_price_queue.insert(0, 135)


# In[4]:


wmt_stock_price_queue # first in first out, let's try


# In[5]:


wmt_stock_price_queue.pop()


# In[6]:


wmt_stock_price_queue.pop()


# In[7]:


wmt_stock_price_queue.pop()


# In[21]:


dir(q)


# In[9]:


from collections import deque
q = deque()


# In[10]:


q.appendleft(5)


# In[11]:


q.appendleft(10)


# In[12]:


q.pop()


# In[13]:


q.pop()


# In[14]:


from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)


# In[15]:


pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})


# In[19]:


pq.size()


# In[17]:


pq.buffer


# In[20]:


# Exercise


# In[49]:


from collections import deque
import time

place_order = deque()  # Global deque to hold orders to be placed
served_order = deque()  # Global deque to hold served orders

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def place_insert_order(self, arr: deque()):
        for i in arr:
            time.sleep(0.5)
            place_order.appendleft(i)  # Add the order to the global deque
            print(f"Placed order: {i}")
            
    def serve_order(self):
        while place_order:
            time.sleep(0.5)
            order = place_order.pop()  # Remove the order from the global place_order deque
            served_order.appendleft(order)  # Add the order to the served_order deque
            print(f"Served order: {order}")
            
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
t = time.time()

if __name__ == '__main__':
    q = Queue()
    q.place_insert_order(orders)
    q.serve_order()
    
print("done in:", time.time() - t)


# In[ ]:





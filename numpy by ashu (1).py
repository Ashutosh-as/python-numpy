#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a=np.array([1,2,3])
print(a)


# In[7]:


a=np.zeros([3,4])
print (a)


# In[9]:


a=np.arange(50,50000,10000)
print(a)


# In[11]:


#lin space
#np.linspace(startnum,endnum,number of point )
z=np.linspace(2,4,3)
print(z)


# In[17]:


#filling same no
import numpy as np
c=np.full((3,3),8)
print(c)


# In[19]:


#for filling an array with random no
import numpy as np
a=np.random.random((3,3))
print(a)


# In[28]:


import numpy as np
a=np.array([1,2,3]),([4,5,6]))
print(a)
print(a.shape)


# In[31]:


a=np.arange(24)
#another np.arrange which take the no of points and print from zero to last no

print(a)


# In[32]:


a.size


# In[36]:


a.shape=(6,4)
print(a.shape[0])
print(a.ndim)
#ndim returns the dimension of array
print(a)
a.dtype
#returns the dtype of an array


# In[39]:


b= np.linspace(3,6,11)
print(b)
print(b.dtype)


# In[41]:


#addition using numpy
import numpy as np
np.sum([10,20])


# In[42]:


a,b,c=10,20,30
np.sum([a,b,c])


# In[46]:


a=[5,8]
b=[2,3]
print(np.subtract(a,b))
print(np.add(a,b))


# In[59]:


a=np.array([5,6])
b=np.array([8,9])
print(np.divide([a],[b]))
print(np.multiply([a],[b]))
print(np.cos(a))
print(np.log(a))


# In[61]:


#array comparision
a=[1,2,3]
b=[4,5,6]
np.equal(a,b)


# In[63]:


a=[1,2,3]
print(np.sum(a))
print(np.max(a))
print(np.mean(a))
print(np.std(a))


# In[65]:


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[1:])


# In[76]:


#array manipulation
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate([a,b],axis=0))


# In[73]:


print(np.stack([a,b],axis=0))
print(np.stack)


# In[77]:


#horizontal stack
import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Horizontal Append:', np.hstack((f, g)))


# In[78]:


## Vertical Stack
import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Vertical Append:', np.vstack((f, g)))


# In[ ]:





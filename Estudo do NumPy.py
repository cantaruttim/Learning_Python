#!/usr/bin/env python
# coding: utf-8

# # Estudo de NumPy

# In[1]:


import numpy as np


# In[2]:


np.__version__


# In[4]:


# Criando um Array

help(np.array)


# In[5]:


# Array unidimensional

vetor1 = np.array([0, 1, 2, 5, 6, 8, 9, 11, 12, 15, 16, 18, 19, 21, 22, 24, 25, 26])
print(vetor1)


# In[6]:


# tipo do array (ndarray)
type(vetor1)


# In[7]:


vetor1.cumsum()


# In[8]:


vetor1[3]


# In[14]:


# Segunda forma de criar arrays

vetor2 = np.arange(.0, 4.5, .5) # start, stop, step
print(vetor2)


# In[15]:


type(vetor2)
np.shape(vetor2)


# In[16]:


x = np.arange(1, 10, 0.25)
print(x)


# In[17]:


np.shape(x)


# In[19]:


print(np.zeros(10)) # para inicializar uma lista de pesos de rede neural profunda


# In[20]:


# função eye

z = np.eye(3)
print(z)


# In[24]:


d = np.diag(np.array([1, 2, 3, 4]))
print(d)


# In[25]:


# utilizando o método linspace, que retorna um número de valores 
# igualmente distribuidos no intervalo específicado

np.linspace(0, 20)


# In[26]:


# podemos retornar valores específicos com o start, stop, step

print(np.linspace(0, 10, 15))


# In[27]:


# podemos converter para log

print(np.logspace(0, 5, 10))


# In[ ]:





# In[ ]:





# In[ ]:





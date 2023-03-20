#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("Produtos.csv", sep = ";")
df


# In[3]:


# df['vl unit faturado'] = df['vl unit faturado'].str.replace(',', '')
# df['vl unit faturado'] = df['vl unit faturado'].astype(float)
# df['anvisa'] = df['anvisa'].astype(str)
df.info()


# In[4]:


# Precisamos converter o vl unit faturado e o vl total faturado para float64

df['vl unit faturado'] = df['vl unit faturado'].str.replace('.' and ',', '')
df['vl total faturado'] = df['vl total faturado'].str.replace('.' and ',', '')


# In[5]:


# convertendo propriamentedito o tipo do dado armazenado nas últimas duas colunas
df['vl total faturado'] = df['vl total faturado'].values.astype('float64')
df['vl unit faturado'] = df['vl unit faturado'].values.astype('float64')


# In[6]:


df.info()


# In[7]:


df[df['qtd. faturada'] > 1]


# In[8]:


# Check point. Alterado o tipo do dado para numérico (float64)
df.to_excel('Produtos.xlsx')


# In[9]:


df['qtd. faturada'].values


# In[10]:


df[df['qtd. faturada'] > 1]


# In[17]:


for i in range(df['qtd. faturada']):
    while (df['qtd. faturada'] != i or df['qtd. faturada'] == i):
        
        df = df.loc[i]
    i += 1


# In[24]:


for i in range(df['qtd. faturada']):
    #print(i)
    
    # quero copiar o valor da linha 
    while i > 1 and ((df['qtd. faturada'] < i) or (df['qtd. faturada'] == 1)) :
        for i in range(df):
            
            df = df.loc[i]

        if i > 1 :
            # transformando o valor do preço para um preço unitário para as quantidades maiores que 1
            df['vl total faturado unitário'] = df['vl total faturado'] / df['qtd. faturada']
            # print(df)
    i += 1


# In[25]:


df.shape


# In[ ]:


df[df['qtd. faturada'] > 1]


# In[ ]:


df['qtd. faturada'].value_counts()


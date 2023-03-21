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

# convertendo propriamentedito o tipo do dado armazenado nas últimas duas colunas
df['vl total faturado'] = df['vl total faturado'].values.astype('float64')
df['vl unit faturado'] = df['vl unit faturado'].values.astype('float64')


# In[5]:


df.info()


# In[6]:


df[df['qtd. faturada'] > 1]


# In[7]:


# Check point. Alterado o tipo do dado para numérico (float64)
df.to_excel('Produtos.xlsx')


# In[8]:


df['qtd. faturada'].values


# In[9]:


df[df['qtd. faturada'] > 1]


# In[43]:


i = 0
j = 0 

for i in df.values:
    for j in df.values:
        
        while i and j != range(df):
            
            df_novo[i][j] = df.iloc[i][j]
            
            i += 1
            j += 1


# In[19]:


for i in range(df['qtd. faturada']):
    for j in range(df['qtd. faturada']):
        
        df_novo[i][j] = df.iloc[i][j]
        
        if i > 1:
            
            df['vl total faturado unitário'] = df['vl total faturado'] / df['qtd. faturada']
return True
       


# In[12]:


for i in df['qtd. faturada']:
    #print(i)
    
    # quero copiar o valor da linha 
    while i > 1 and df['qtd. faturada'] == 1:
        df_novo[i] = df.iloc[i]    
        
        if i > 1 :
            # transformando o valor do preço para um preço unitário para as quantidades maiores que 1
            df['vl total faturado unitário'] = df['vl total faturado'] / df['qtd. faturada']
            # print(df)
        else:
            break
    i += 1


# In[ ]:


df.shape


# In[ ]:


df[df['qtd. faturada'] > 1]


# In[ ]:


df['qtd. faturada'].value_counts()


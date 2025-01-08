#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.read_csv('campeonato-brasileiro-full.csv')


# In[ ]:


# Apresente os 5 primeiros 


# In[7]:


df.head()


# In[ ]:


# Localize a linha 310. qual jogo e qual data foi realizada a partida


# In[49]:


linha = df.loc[310,['data','mandante','visitante']]


# In[47]:


print(linha)


# In[1]:


#quantos gols foram feitos no campeonato no total


# In[7]:


total = df['mandante_Placar'].sum() + df['visitante_Placar'].sum()


# In[8]:


total


# In[9]:


# Qual o horário que teve mais jogos no campeonato


# In[23]:


df['hora'].value_counts().head(1)


# In[24]:


# E em qual dia da semana


# In[ ]:





# In[ ]:





# In[25]:


# Qual time mais empatou como mandante


# In[42]:


emp = df [df['mandante_Placar'] == df['visitante_Placar']]


# In[46]:


mandante= emp.groupby('mandante').size()


# In[50]:


MandanteEmpate = mandante.sort_values(ascending=False)


# In[52]:


MandanteEmpate.head()


# In[53]:


# Qual time mais empatou como mandante


# In[55]:


emp = df[df['mandante_Placar'] == df['visitante_Placar']]


# In[56]:


empate = emp.groupby('visitante').size()


# In[57]:


visitEmpate = empate.sort_values(ascending = False)


# In[59]:


visitEmpate.head()


# In[60]:


# Time com maior número de gols como mandante


# In[ ]:





# In[64]:


mv = df.groupby('mandante')


# In[70]:


m = mv['mandante_Placar'].sum()


# In[71]:


mng = m.sort_values(ascending = False)


# In[72]:


mng.head()


# In[73]:


# Crie uma coluna apenas com o Ano da partida e responda qual time mais empatou como mandante no ano de 2019


# In[88]:


df['Ano'] = df['data'].str[-4:]


# In[133]:


df['Ano'] = df['Ano'].astype(int)


# In[136]:


emp = df[(df['mandante_Placar'] == df['visitante_Placar'])& (df['Ano'] == 2019)]


# In[148]:


emp1 = emp.groupby('mandante').size()


# In[150]:


NEmpateMandante = emp1.sort_values(ascending = False)


# In[155]:


NEmpateMandante.head()


# In[ ]:





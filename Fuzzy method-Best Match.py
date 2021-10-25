#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv


# In[6]:


with open("drug links.csv") as filecsv:
    reader=csv.reader(filecsv,delimiter=",")
    #header= next(lettore)
    #print(header)
    name_en=[]
    for name in reader:
        if name[1] not in name_en:
            name_en.append(name[1])
#print(name_en)


# In[7]:


name_it1=[]
with open('Classe_A_per_principio_attivo_15-04-2021.csv') as filecsv:
    reader=csv.reader(filecsv,delimiter=';')
    #header=next(reader)
    #print(header)
   
    for name in reader:
        if name[0] not in name_it1:
            name_it1.append(name[0])
#print(name_it1)


# In[8]:


name_it1.pop()


# In[9]:


with open('Classe_H_per_principio_attivo_15-04-2021.csv') as filecsv:
    reader=csv.reader(filecsv,delimiter=';')
    
    name_it2=[]
    for name in reader:
        if name[0] not in name_it2:
            name_it2.append(name[0])
#print(name_it2)


# In[10]:



from fuzzywuzzy import fuzz


# In[11]:


name_it=name_it1+name_it2


# In[12]:


set_it=set(name_it)
set_en=set(name_en)


print(len(name_it))
print(len(set_it))
print(len(name_en))
print(len(set_en))


# 1 RATIO  
# The standard Levenshtein distance similarity ratio between two sequences
# 

# In[14]:


match=[]
for x in set_it:
    dist_sum=[]
    for y in set_en:
        dist=fuzz.ratio(x.lower(),y.lower())
        dist_sum.append((dist,(x,y)))
    
    match.append(max(dist_sum))  


# In[23]:


high=[]
for (z,(x,y)) in match:
    if z>=75:
        high.append((z,(x,y)))
    
print(len(high))
#print(high)


# In[16]:


low=[] #not reliable
for (z,(x,y)) in match:
    if 60<z<75:
        low.append((z,(x,y)))
    
print(len(low))
#print(low)


# In[2]:


#print(len(high))
#for z,(x,y) in high:
    #print((x))


# 2 TOKEN     
# Sorted alphabetically and then joined together

# In[17]:


match2=[]
for x in set_it:
    dist_sum2=[]
    for y in set_en:
        dist=fuzz.token_sort_ratio(x,y)
        dist_sum2.append((dist,(x,y)))
    match2.append(max(dist_sum2)) 


# In[24]:


high2=[]
for (a,(s,d)) in match2:
    if a>=75:
        high2.append((a,(s,d)))
print(len(high2))
print(high2)


# In[19]:


low2=[] #not reliable
for (z,(x,y)) in match2:
    if 70<z<75:
        low2.append((z,(x,y)))
    
print(len(low2))
#print(low2)


# 3 Try to mix                    
# Set high and high2

# In[25]:


mixed=high+high2
mixed_set=set(mixed)
print(len(mixed_set))
print(len(high))
print(len(high2))
print(mixed_set)

        


# In[27]:


#sort alfabet.

onlyx=[]
for z,x in mixed_set:
    onlyx.append(x)
onlyx.sort(key=lambda x: x[0])  

print(len(onlyx))
print(onlyx)

#export
    


# In[28]:


with open("Best_Match.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(onlyx)


# In[ ]:





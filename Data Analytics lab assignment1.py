#!/usr/bin/env python
# coding: utf-8

# 1.Problem Statement:
# 
# To find the frequency of unique words in a document and arrange them in a vector based on ASCII order in Python.

# In[7]:


# open and read the document file
file_path="C:/Users/gazala parveen/OneDrive/Documents/The Zen of Python, by Tim Peters.txt"
with open(file_path, "r" ) as docu:
    text=docu.read()

#convert the text to lowercase
text=text.lower()

#Remove Seperators
text=text.replace(".","").replace(",", "").replace("!","").replace("?","").replace("--","").replace("*","")

#split the text into words
words=text.split()
print(words)
    


# In[8]:


#take a empty dictionary data structure to store word counts
words_count={}


#Now using loop to count the frequency of the words
for word in words:
    if word in words_count:
        words_count[word]+=1
    else:
        words_count[word]=1

#Sorting the keys(words) as per Ascii 
sorted_by_key=dict(sorted(words_count.items()))


#The displayed output is as follows
for word,count in sorted_by_key.items():
     print(f"'{word}': {count}")
        
        


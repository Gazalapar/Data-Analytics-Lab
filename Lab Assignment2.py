#!/usr/bin/env python
# coding: utf-8

# 2.problem Statement
# To find common words between two documents and display their frequencies along with how many times they appear in each document
# 

# In[9]:


from collections import Counter

#To read the content of a file and return the word frequencies
def get_word_freq(document_name):
    with open(document_name, "r") as docu:
        text=docu.read().lower()
    words=text.split()
    return Counter(words)


#To find the common words and their frequencies in both documents
def find_common_words(document1,document2):
    freq1=get_word_freq(document1)
    freq2=get_word_freq(document2)
    
    #common words by taking intersection of both counters
    common_words=freq1 & freq2
    
    # Create a dictionary of common words with their frequencies in both documents
    common_freq = {word: (freq1[word], freq2[word]) for word in common_words}
    
    return common_freq




document1="C:/Users/gazala parveen/OneDrive/Documents/Document1.txt"
document2="C:/Users/gazala parveen/OneDrive/Documents/Document2.txt"
common_frequencies=find_common_words(document1,document2)

#common words and their frequencies along with file name
print("Common words in both documents:")
for word,(freq1,freq2)in common_frequencies.items():
    print(f"'{word}': {freq1} times in D1 and {freq2} times in D2")

    
    
    


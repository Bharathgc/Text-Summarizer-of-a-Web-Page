#!/usr/bin/env python
# coding: utf-8

# In[81]:


import bs4 as bs
import urllib.request
import re
import nltk
import heapq


# In[82]:


#get the data from the paragraph
page = urllib.request.urlopen("https://en.wikipedia.org/wiki/Artificial_neural_network").read()    


# In[83]:


#if you want to see the data in structured format
print(soup.prettify)


# In[84]:


paragraphtext = ""
# i will extract all the data under paragraph <p> tag
tag = 'p'
for paragraph in soup.find_all('p'):
    paragraphtext += paragraph.text
print(paragraphtext)


# In[85]:


#clean the data
# remove all the bracketes like [1][2][3] .. etc and replace it with single space
text = re.sub(r'\[[0-9]*\]',' ',text)
# remove all extra spaces and replace it with single space
text = re.sub(r'\s+',' ',text)    
clean_text = text.lower()
# remove punctutations
clean_text = re.sub(r'\W',' ',clean_text)
# remove digits
clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)
sentences = nltk.sent_tokenize(text)
stop_words = nltk.corpus.stopwords.words('english')
print(sentences)


# In[86]:


wordlist = [word for word in nltk.word_tokenize(clean_text) if word not in stop_words ]
for word in wordlist:
    word2count[word] = wordlist.count(word)
            
#calculate the weighted histogram
for key in word2count.keys():                   
    word2count[key]=word2count[key]/max(word2count.values())


# In[87]:


# Calculate the score   
sent2score = {}
for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' '))<30:
                if sentence not in sent2score.keys():
                     sent2score[sentence]=word2count[word]
                else:
                    sent2score[sentence]+=word2count[word]


# In[88]:


best_sentences = heapq.nlargest(7,sent2score,key=sent2score.get)
for sentences in best_sentences:
    print(sentences,'\n')


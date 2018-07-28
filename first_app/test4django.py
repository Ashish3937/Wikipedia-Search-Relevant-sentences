import wikipedia
from collections import OrderedDict
import re
import nltk
import os
from nltk.tokenize import sent_tokenize

nltk.download('punkt')



pattern=re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s\d?\d?\s?[1-2][0-9][0-9][0-9]')
pattern2=re.compile(r'[1-2][0-9][0-9][0-9]')
pattern3 = re.compile(r'([A-Z][^\.!?]*[\.!?])')


def main(query,num):
    a=query
    b=int(num)
    search=wikipedia.search(a)
    if len(search)==0:
        return ["No relevant page found","Search with appropriate keywords"]
    else:

        search2=[]
        for i in search :
            if i.isupper()==False:
                search2.append(i)
        d=search[0]
        content=wikipedia.WikipediaPage(title=d).content
        content=re.sub(r'\([^)]*\)', '',content)
        content3=sent_tokenize(content)


        new_content=[]
        new_content1=[]

        for i in content3:
            if pattern3.findall(i):
                new_content1.append(i)


        for i in new_content1:
            if pattern.findall(i):
                new_content.append(i)

        dict1={}
        for i in range(0,len(new_content)):

            k=pattern2.findall(new_content[i])
            key=k[0]
            if key in dict1:
                dict1[key]+=new_content[i]
            else:
                dict1[key]=new_content[i]
        dict1=OrderedDict(sorted(dict1.items(), key=lambda t: t[0]))
        dict1=dict(dict1)
        content_list=list(dict1.values())
        content_str=' '.join(content_list)
        content4=sent_tokenize(content_str)
        content5=[search[0]]
        


        if b>=len(content4):
            
            return content5+content4
        else:
            
            for i in range(0,b):
                content5.append(content4[i])
            return content5

        
        


  




     
    
       
 
    
    

    
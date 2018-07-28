
import wikipedia
from collections import OrderedDict
import re
import spacy

nlp=spacy.load('D:/files/unfound/test/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
pattern=re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s\d?\d?\s?[1-2][0-9][0-9][0-9]')
pattern2=re.compile(r'[1-2][0-9][0-9][0-9]')
pattern3 = re.compile(r'([A-Z][^\.!?]*[\.!?])')


def main(query,num):
    a=query
    b=num
    search=wikipedia.search(a)
    if len(search)==0:
        print("No relevant pages found")
    else:
        
        search2=[]
        for i in search :
            if i.isupper()==False:
                search2.append(i)
        d=search[0]
        content=wikipedia.WikipediaPage(title=d).content
        content=re.sub(r'\([^)]*\)', '',content)
        content2=nlp(content)
        
        content3 = [sent.string.strip() for sent in content2.sents]
        print(type(content3))
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
        content_list=nlp(content_str)
        content4 = [sent.string.strip() for sent in content_list.sents]
        
        if b>len(content):
            b=len(content)
        for i in range(0,b):
            print(content4[i])
        
        
        


query=str(input("Enter the query:"))
number=int(input("Enter the number of sentences:"))    
main(query,number)



     
    
       
 
    
    

    
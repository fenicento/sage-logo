'''
Created on Sep 18, 2013

@author: davide
'''
from itertools import combinations
import json

json_data=open('tagAnalysis2.json')
json_data2=open('tagsOnly2.json')
a = json.load(json_data)
b = json.load(json_data2)

c=list()
#print b

a=a[:50]
siz=[i[1] for i in a]
a=[i[0] for i in a]


links=list()
nodes=list()

for l in b:
    foundk=list()
    count=0
    print l['file']
    for tag in l['tags']:
        if tag in a:
            foundk.append(tag)
            print tag
            count=count+1
    
    if count>1:
        for z in combinations(foundk,2):
            found = False
            for link in links:
                if (link['source'] == a.index(z[0]) and link['target'] == a.index(z[1])) or  (link['source'] == a.index(z[1]) and link['target'] == a.index(z[0])):
                    link['value'] = link['value']+1
                    found = True
                
            if not found:
                link={
                      'source' : a.index(z[0]),
                      'target' : a.index(z[1]),
                      'value' : 1
                      }
                links.append(link)

for idx,el in enumerate(a):
    s={
       'name':el,
       'group':1,
       'size':siz[idx]
       }
    nodes.append(s)
                 
print nodes
print links

d={
   'nodes':nodes,
   'links':links
   }
with open('tagGraph2.json', 'wb') as fp:
    json.dump(d,fp)
    
    
    
            
            
            
    
    


from xml.dom import minidom
import io,json
from collections import Counter

res=[]
biglist = []
fin = []

import glob
lis = glob.glob('rekeywordwidget/*.xml')
#xmldoc = minidom.parse('items.xml')
for l in lis:
	print l
	obj={"file":l,"tags":[]}
	xmldoc = minidom.parse(l)
	ks = xmldoc.getElementsByTagName("kwd")
	for k in ks:
		obj['tags'].append(k.firstChild.nodeValue.lower())
		biglist.append(k.firstChild.nodeValue.lower())

	res.append(obj)

for c in Counter(biglist):
	fin.append([c,Counter(biglist)[c]])

fin = sorted(fin, key=lambda student: student[1], reverse=True)

print fin

with io.open('tagAnalysis2.json', 'w', encoding='utf-8') as f:
	f.write(unicode(json.dumps(fin, indent=4,ensure_ascii=False)))

with io.open('tagsOnly2.json', 'w', encoding='utf-8') as f:
	f.write(unicode(json.dumps(res, indent=4,ensure_ascii=False)))






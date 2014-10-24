import csv,json


res = []

with open('conceptsinBDS.csv', 'rbU') as csvfile:
	 spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	 headers = spamreader.next()

	 obj={}

	 for row in spamreader:
		if row[0]!="":
			res.append(obj)
			obj={"id":row[0],"tags":[row[1]]}
		else:
			obj['tags'].append(row[1])

links=list()
nodes=list()

res.remove({})

for r in res:
	for t in r['tags']:
		
		if len(nodes)==0:
			
			nodes.append({"id":t,"size":1})
		else:
			found = any(x["id"] == t for x in nodes)
			if not found:
				nodes.append({"id":t,"size":1})
			else:
				el = [elem for elem in nodes if elem['id'] == t][0]
				el['size'] = el['size']+1

print json.dumps(nodes,indent=4)


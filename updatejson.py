import json

with open("update.js", "r+") as sfile:
    	sdata = json.load(sfile)
    	for i in range (len(sdata)):
		sdata[i][u'name'] = sdata[i]['url']
with open("updated.js", "r+") as tfile:
		json.dump(sdata, tfile)
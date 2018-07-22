#!/usr/bin/python

name = raw_input("Please input name:")
info = {}
#print type(name)
age = raw_input("Please input age:")
gender=raw_input("Please input gender(M/F):")
info['name']=name
info['age']=age
info['gender']=gender
#print info
#print info.items()
#for i in info.items():
#	print i
for k,v in info.items():
	print k+':'+v
	print "%s : %s"%(k,v)


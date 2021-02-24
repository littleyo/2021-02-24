#!/usr/bin/env python3
#
count={0:[''],1:[''],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'],'*':[''],0:[''],'#':['']}
#print(count[2])

#ouput result
def toPrint(result):
	#print(len(result))
	for i in range(len(result)):
		print(result[i]),

#['a']['b']->['ab']
def toAcc(m,n):
	q=[]
	w=[]
	for i in range(len(m)):
		for j in range(len(n)):
			q.append(str(m[i])+str(n[j]))
			#print(q)
	w.append(q)
	return w

def toSplit(t,p):
	first=t
	if len(p)==1:
		second=p[0]
		c=toAcc(first,second)
		return c
	else:
		v=p[0]
		u=p[1:]
		#print(v,u)
		c=toSplit(t,toSplit(v,u))
		return c


#default list
a=[3,2,5,'*',1,6]
if len(a)==1:
	toPrint(count[a[0]])
	
b=[]
for i in a:
	b.append(count[i])

result=toSplit(b[0],b[1:])
toPrint(result[0])





	
	
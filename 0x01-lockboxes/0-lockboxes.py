#!/usr/bin/python3
def canUnlockAll(boxes):
	viseted=[]
	successeur=boxes[0]
	while  successeur:
		i=successeur.pop()
		if i not in viseted:
			viseted.append(i)
			for j in range (len(boxes[i])):
				successeur.append(boxes[j])
	for i in range (len(boxes)):
		for j in range (len(boxes[i])):
			if j not in  viseted:
				return False 
	return False
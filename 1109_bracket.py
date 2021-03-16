# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
def bracket(l,r):
	if(l==0 and r==0):
		return 1
	else:
		if(l == 0):
			return 1
		elif (l<r):
			return bracket(l-1,r)+bracket(l,r-1)
		else:
			return bracket(l-1,r)
	
answer=bracket(user_input,user_input)
print(answer)
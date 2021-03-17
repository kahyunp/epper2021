# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
N,R= map(int, input().split())
n=list(map(int,input().split()))
r=[]
for i in range (R):
		r.append(list(map(int,input().split())))
goal=int(input())

def solution(N,R,n,r,goal):
	n.insert(0,0)
	indegree=[0 for i in range(N+1)]
	adj=[[0]*(N+1) for i in range(N+1)]
	queue=deque()
	time=[0 for i in range(N+1)]
	for i in r:
		adj[i[0]][i[1]]=1
		indegree[i[1]]+=1
	for i in range(1,N+1):
		if(indegree[i]==0):
			queue.append(i)
			time[i]=n[i]
	while queue:
		p=queue.popleft()
		for i in range(1,N+1):
			if(adj[p][i]==1):
				time[i]=max(time[p]+n[i],time[i])
				indegree[i]-=1
				if(indegree[i]==0):
					queue.append(i)
	print(time[goal])
	
solution(N,R,n,r,goal)
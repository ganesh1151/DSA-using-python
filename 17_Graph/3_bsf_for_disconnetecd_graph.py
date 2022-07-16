from collections import deque

def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def BSF(adj,s,visited):
    q=deque()
    q.append(s)
    visited[s]=True

    while q:
        s=q.popleft()
        print(s,end=" ")

        for u in adj[s]:
            if visited[u]==False:
                q.append(u)
                visited[u]=True

def BFSDis(adj):
    visited=[False]*len(adj)

    for u in range(len(adj)):
        if visited[u]==False:
            BSF(adj,u,visited)

def printGraph(adj):
    for u,l in enumerate(adj):
        print(u,l)

#main

v=7

adj=[[1,2],[0,3],[0,3],[1,2],[5,6],[4,6],[4,5]]

printGraph(adj)

print("\nBSF path")
BFSDis(adj)
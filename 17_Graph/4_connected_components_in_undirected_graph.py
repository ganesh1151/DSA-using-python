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
                visited[u]=t=True
    print()

def BSFDis(adj):
    visited=[False]*len(adj)
    res=0
    for u in range(len(adj)):
        if visited[u]==False:
            res+=1
            BSF(adj,u,visited)

    return res

def printGraph(adj):
    for u,l in enumerate(adj):
        print(u,l)


#main

v=8

adj=[[1,2],[0,2],[0,1],[4],[3],[6,7],[5],[5]]

printGraph(adj)

print("\nConnected Components")
print("no of connected components",BSFDis(adj))

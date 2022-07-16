def DFSRec(adj,s,visited):
    visited[s]=True

    print(s,end=" ")

    for u in adj[s]:
        if visited[u]==False:
            DFSRec(adj,u,visited)

def DFS(adj,s):
    visited=[False]*len(adj)
    DFSRec(adj,s,visited)

def printGraph(adj):
    for u,l in enumerate(adj):
        print(u,l)

adj=[[1,2],[0,3,4],[0,3],[1,2,4],[1,3]]

printGraph(adj)

DFS(adj,0)
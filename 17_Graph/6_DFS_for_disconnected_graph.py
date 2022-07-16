def DFSRec(adj,s,visited):
    visited[s]=True

    print(s,end=" ")

    for u in adj[s]:

        if visited[u]==False:
            DFSRec(adj,u,visited)

def DFS(adj):
    visited=[False]*len(adj)

    for u in range (len(adj)):
        if visited[u]==False:
            DFSRec(adj,u,visited)

def printGraph(adj):

    for u,l in enumerate(adj):
        print(u,l)

adj=[[1,2],[0,2],[0,1],[4],[3]]

printGraph(adj)

DFS(adj)

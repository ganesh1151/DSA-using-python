def DFSRec(adj,s,visited):
    visited[s]=True

    print(s,end=" ")

    for u in adj[s]:
        if visited[u]==False:
            DFSRec(adj,u,visited)

def DFS(adj):
    visited=[False]*len(adj)
    res=0
    for u in range(len(adj)):
        if visited[u]==False:
            res+=1
            DFSRec(adj,u,visited)
            print()
    return  res

def printGraph(adj):
    for u,l in enumerate(adj):
        print(u,l)

adj=[[1,2],[0,2],[0,1],[4],[3]]

printGraph(adj)

print("conneted component")
print("no of connected component ",DFS(adj))
#21/4
from collections import defaultdict,deque
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self,start):
        visited=set()
        result=[]
        def dfs_util(v):
            visited.add(v)
            result.append(v)
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    dfs_util(neighbour)
            
        dfs_util(start)
        return result
    def bfs(self,start):
        visited=set()
        queue=deque([start])
        result=[]
        visited.add(start)
        while queue:
            vertex=queue.popleft()
            result.append(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
        return result
V=int(input("enter number of vertices"))
E=int(input("enter number of edges"))
g=Graph(V)
print("enter edges(u,v):")
for i in range(E):
    u,v=map(int,input().split())
    g.addedge(u,v)
start=int(input("enter starting vertex:"))
dfs_result=g.dfs(start)
bfs_result=g.bfs(start)
print("\nDFS traversal:",dfs_result)
print("\nBFS traversal:",bfs_result)

        
    
        
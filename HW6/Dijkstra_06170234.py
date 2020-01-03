from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        
    def min_distance(self, dist, min_dist_set):
        min_dist = float("inf")
        for v in range(self.V):
            if dist[v] < min_dist and min_dist_set[v] == False:
                min_dist = dist[v]
                min_index = v
        return min_index
        
    def Dijkstra(self, s): 
        dist = [float("inf")] * self.V
        dist[s] = 0
        min_dist_set = [False] * self.V
        for count in range(self.V):
            u = self.min_distance(dist, min_dist_set)
            min_dist_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and min_dist_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    
        dist_dict = { str(i): dist[i] for i in range(len(dist)) }
        return dist_dict
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def Kruskal(self):
        result =[]
        i = 0
        e = 0
        parent = []
        rank = []
        for node in range(self.V):
            rank.append(-1)

        for node in range(self.V):
            parent.append(node)

        while e < self.V -1 :
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            if x != y:
                e = e + 1  
                result.append([u,v,w])
                self.union(parent, rank, x, y)  
        
        
        output = {}
        for u, v, w in result:
            output[str(u)+'-'+str(v)]  = w
        return output

# Minimum Spanning Tree
* 不能有迴路:因為如果有迴路那邊就是N條了，而不是N-1了，那為啥是N-1呢？因為一個邊能連兩個定點，N個定點不留孤島肯定是N-1條邊連起來；假設迴路構成的路徑總和最短，那我們去掉迴路中一條最長的，那剩下的是不更短？而且其餘頂點還保持連通？所以有迴路一定不是最短
* 是一種用來尋找最小生成樹的演算法，新建圖G，G中擁有原圖中相同的節點，但沒有邊將原圖中所有的邊按權值從小到大排序從權值最小的邊開始，如果這條邊連接的兩個節點於圖G中不在同一個連通分量中，則添加這條邊到圖G中，重複3，直至圖G中所有的節點都在同一個連通分量中。根據邊的加權值以遞增的方式，一次找出加權值最低的邊來構建最小生成樹，而且規定：每次新增的邊不能造成生成樹有迴路，知道找到N-1個邊為止。

![image](https://github.com/hans0517/hans/blob/master/images/MST.jpg)
```python
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
```
# Shortest Path
* 通過為每個頂點v保留目前為止所找到的從s到v的最短路徑來工作的。初始時，源點s的路徑長度值被賦為0，把所有其他頂點的路徑長度設為無窮大，即表示我們不知道任何通向這些頂點的路徑。當演算法結束時，d[v]中儲存的便是從s到v的最短路徑，或者如果路徑不存在的話是無窮大。Dijstra演算法的基礎操作是邊的拓展:如果存在一條從u到v的邊，那麼從s到u的最短路徑可以通過將邊(u,v)添加到尾部來拓展一條從s到v的路徑。這條路徑的長度是d[u]+w(u,v)。如果這個值比目前已知的d[v]的值要小，我們可以用新值來替代當前d[v]中的值。拓展邊的操作一直執行到所有的d[v]都代表從s到v最短路徑的花費。這個演算法經過組織因而當d[u]達到它最終的值的時候沒條邊(u,v)都只被拓展一次。演算法維護兩個頂點集S和Q。集合S保留了我們已知的所有d[v]的值已經是最短路徑的值頂點，而集合Q則保留其他所有頂點。集合S初始狀態為空，而後每一步都有一個頂點從Q移動到S。這個被選擇的頂點是Q中擁有最小的d[u]值的頂點。當一個頂點u從Q中轉移到了S中，演算法對每條外接邊(u,v)進行拓展。

![image](https://github.com/hans0517/hans/blob/master/images/shortestpath.jpg)
```python
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
```

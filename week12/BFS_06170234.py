from collections import defaultdict
  
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
   
    def BFS(self, s):
        seen = []
        queue = []
        queue.append(s)
        
        while (len(queue)>0):
            current_node = queue.pop(0) #第一個點為要看的點
            near = self.graph[current_node] #要看的點的鄰點
            if current_node not in seen: #如果點還沒在seen裡，就加進去(seen是走訪過的[])
                seen.append(current_node)
                for w in near:
                    queue.append(w)
            
            if len(queue) == 0: #直到queue被拿完後，就回傳答案
                return seen
        return seen

from collections import defaultdict
  
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
    
    def DFS(self, s):
        seen = []
        stack = []
        stack.append(s)
        
        while (len(stack)>0):
            current_node = stack.pop() #要看的點
            near = self.graph[current_node] #要看的點的鄰點

            if current_node not in seen:
                seen.append(current_node) #如果要看的點不在seen裡，就加進seen
                for w in near: #一樣從near裡抓出每個值
                    if w not in stack: #如果near裡的值不在stack裡
                        if w not in seen: #加上不在seen裡
                            stack.append(w) #就加入stack裡
                    
            if len(stack) == 0: #直到stack被拿完後，就回傳答案
                return seen
        return seen

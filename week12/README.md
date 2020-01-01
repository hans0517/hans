# BFS
* 使用Queue
* 空間複雜度為O(|V|+|E|)，|V|是節點數目，|E|是圖中邊的數目
* 時間複雜度為O(|V|+|E|)，|V|是節點數目，|E|是圖中邊的數目
* 從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置， 無論如何都要遍歷完畢整張地圖才終止。 按照就近原則進行， 距離原點相同的節點的訪問順序是相近的


## BFS課堂練習
![image](https://github.com/hans0517/hans/blob/master/week12/1129.jpg)

## BFS code

```python
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
 ```

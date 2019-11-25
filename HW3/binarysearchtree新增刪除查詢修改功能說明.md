# BinarySearchTree(BST)
## 新增
* 1.新增Node時，如果比root小要放左邊，比root大要放右邊，都要照著左小右大的原理依序比較，最後排進去，所以可以知道最左邊的葉子節點是最小的，最右邊的葉子節點是最大的
* 2.功能:欲插入BST的數能擺放到正確位置，並不破壞BST規則(左小右大)
```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insert(self, root, val):
        self.root = root
        self.val = val
        if root == None: #如果root原本沒有東西的話，新的節點即為root
            root = TreeNode(val)
        elif val <= root.val: #如果val的值小於root的值，放左邊，並討論左邊如果沒有值以及有值的時候
            if root.left != None:
                return self.insert(root.left, val)
            else:
                root.left = TreeNode(val)
                return root.left
        elif val > root.val: #如果val的值大於root的值，放右邊，並討論左邊如果沒有值以及有值的時候
            if root.right != None:
                return self.insert(root.right, val)
            else:
                root.right = TreeNode(val)
                return root.right
```
## 刪除
* 1.在刪除節點時，有分成三種情況，第一種是完全沒有子節點(no child)，第二種是只有一個子節點(only leftchild or rightchild)，第三種是有兩個子節點
* 2.完全沒有子節點，直接刪除該節點即可
* 3.有一個子節點，刪除該節點(a)時，將其唯一子節點(b)取代，並將pointer指向正確位置，這時a的parent指向b
* 4.功能:欲刪除某個節點時，能正確將刪除的節點用正確的數取代，並將pointer指向對的parent或child
```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def find(self, parent, root, target): #find放了3個參數
        if root == None: #如果root是空的，那就會find不到，找不到直接回傳None
            return None, None
        elif root != None: #如果root不是空的，分成幾種情況
            if root.val == target: #如果root等於要找的target
                return (parent, root) #回傳parent和root本身，因為有設三個變數，須把parent也return
            elif root.val > target: #如果root大於target
                return self.find(root, root.left, target) #把root當成parent，並繼續往左邊找
            elif root.val < target: #如果root小於target
                return self.find(root, root.right, target) #跟大於一樣，只是如果是小於，要往右邊找
    
    def del_min(self, node): #刪掉最小值
        if node.left==None: #如果進來節點的左邊沒有值，代表沒有最小值
            return node.val, node.right #直接回傳此節點值和右邊較大的點
        else: #剩下是如果進來節點的左邊有值
            val, node.left = self.del_min(node.left) #就看node.left.left是否有值，再跑del_min
            #會變成如果node.left.left空就回傳node.left.val,node.left.right
            return val, node
    
    def delete(self, root, target):
        while self.find(None, root, target) != (None, None):
            parent, node = self.find(None, root, target) #先用find找到node還有其parent
            if node.left == None or node.right == None: #有左或右一個child
                if parent != None: #如果節點也有parent
                    if parent.left == node: #如果此節點在parent的左邊
                        if node.left:
                            parent.left = node.left
                        if node.right:
                            parent.left = node.right
                        if node.left== None and node.right == None:
                            parent.left = None
                        # 如果節點存在的子節點是在左，那就把左子節點接到parent的左邊
                        # 反之，存在的子節點是右，也是直接接到parent的左邊，那麼原本的node就會被取代掉
                    elif parent.right == node: #如果此節點在parent的右邊
                        if node.left:
                            parent.right = node.left
                        if node.right:
                            parent.right = node.right
                        if node.left== None and node.right == None:
                            parent.right = None
                        #與上面相同道理，只是把node設在parent的右子節點
            else:
                right_min, node.right = self.del_min(node.right) #
                node.val = right_min
        return root
```                
## 查詢
* 1.如果有重複的值，回傳離root最近的那個
* 2.功能:查詢欲查詢之數是否在正確位置上
* 3.如果搜尋失敗，回傳None
```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def search(self, root, target):
        self.root = root
        self.target = target
        if not root: #如果root不存在，表示search不到，直接回傳None
            return None
        elif root.val == target: #如果root與target相等，search可直接回傳root值
            return root
        elif root.val < target: #如果root比target小(target比root大)，要繼續往右search
            return self.search(root.right, target)
        elif root.val > target: #如果root比target大(target比root小)，要繼續往左search
            return self.search(root.left, target)
 ```
## 修改
* 1.功能:可以輸入想被更改的數和要取代的數，相新的數取代掉要改的那個數
* 2.如果有重複值，比如BST裡面有兩個3，然後想用6去修改，那麼兩個3都要改成6，因此BST會變成有兩個6
```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def modify(self, root, target, new_val):
        if root.val == target:
            root.val = new_val
        elif root.left or root.right:
            if root.left != None:
                self.modify(root.left, target, new_val)
            if root.right != None:
                self.modify(root.right, target, new_val)
        return root
```

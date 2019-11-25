class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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
        
    def modify(self, root, target, new_val):
        if root.val == target:
            root.val = new_val
        elif root.left or root.right:
            if root.left != None:
                self.modify(root.left, target, new_val)
            if root.right != None:
                self.modify(root.right, target, new_val)
        return root
# 參考資料:放在學習歷程ipynb檔裡

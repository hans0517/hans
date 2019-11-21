# BinarySearchTree(BST)
## 新增
* 1.新增Node時，如果比root小要放左邊，比root大要放右邊，都要照著左小右大的原理依序比較，最後排進去，所以可以知道最左邊的葉子節點是最小的，最右邊的葉子節點是最大的
* 2.功能:欲插入BST的數能擺放到正確位置，並不破壞BST規則
```python
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
* 4.功能:欲刪除
## 查詢
* 1.如果有重複的值，回傳離root最近的那個
## 修改

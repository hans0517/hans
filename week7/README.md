# Merge Sort
[學習歷程-ipynb檔連結](https://github.com/hans0517/hans/blob/master/HW2/mergesort%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.ipynb)
* Merge Sort屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，最初先將數列分成兩半，再一直分到剩兩個兩個一組，如果總數為奇數，則剩的數自己一組，兩個兩個比大小，小的放左，大的放右，合併後比較，'依序'比較，比到最後完成排序
![image](https://github.com/hans0517/hans/blob/master/week7/MS%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)

```python
class Solution(object):
    def merge_sort(self, nums):
        if len(nums)<2: #設定限制，以防進入無限迴圈
            return nums
        else:
            middle = len(nums)//2
            left = nums[:middle]
            right = nums[middle:] #依照middle，把nums切成兩半
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i = i+1 #如果左邊的數小於右邊的，將左邊的數加到空的nums的k
                    k = k+1
                else:
                    nums[k] = right[j]
                    j = j+1 #跟以上同邏輯，右邊的加進去
                    k = k+1 #k要跟著移動，加完一個要繼續到下一個位置
            while i < len(left) or j < len(right):
                if i < len(left):
                    nums[k] = left[i]
                    i = i+1
                    k = k+1
                if j < len(right):
                    nums[k] = right[j]
                    j = j+1
                    k = k+1
            return nums
          
nums = [-2, 6, 7, -4, 0, 3, -1, 4]
Solution().merge_sort(nums)
```

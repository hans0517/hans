# Heap Sort
* [學習歷程-ipynb檔連結](https://github.com/hans0517/hans/blob/master/HW2/heapsort%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.ipynb)
* 學習網站 : https://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html
* 若以升序排序說明，把陣列轉換成最大堆積(Max-Heap Heap)，這是一種滿足最大堆積性質(Max-Heap Property)的二元樹：對於除了根之外的每個節點i, A[parent(i)] ≥ A[i]。重複從最大堆積取出數值最大的結點(把根結點和最後一個結點交換，把交換後的最後一個結點移出堆)，並讓殘餘的堆積維持最大堆積性質。
![image](https://github.com/hans0517/hans/blob/master/week6/heapsort.png)
```python
class Solution(object):
    def heap_sort(self, nums):
        n = len(nums) #設n為list的長度
        for i in range(n - 1, -1, -1): #從最後一個數開始n-1,n-2,n-3.........直到0
            self.heapify(nums, i, n, compare) #i值一直換，丟入heapify function裡
        for i in range(n - 1, 0, -1): #從最後面開始跑迴圈(尾，頭，往前推一個)
            nums[0], nums[i] = nums[i], nums[0] #這邊是要排序，拿出去值後，第一個數要和最後一個數互換，繼續排列，直到排完，所以也是跑迴圈
            self.heapify(nums, 0, i, compare)
        return nums

    def compare(a, b):
        if a < b:
            return -1
        if a > b:
            return 1 #這邊設定一個用來比較的參數compare，如果帶入的值a<b，回傳-1，a>b回傳1
        return 0

    def heapify(self, nums ,index, size, compare):
        largest = index #設index為最大父節點
        rightindex = 2 * index + 2 #父節點index的右子節點在位置(2index+2)
        leftindex = 2 * index + 1 #父節點index的左子節點在位置(2index+1)
        if leftindex < size and compare(nums[leftindex], nums[largest]) > 0:
            largest = leftindex #如果左邊的子節點存在，運用compare function表較，>0代表a>b，左邊的子節點則變成父節點
        if rightindex < size and compare(nums[rightindex], nums[largest]) > 0:
            largest = rightindex #如果右邊的子節點存在，運用compare function表較，>0代表a>b，右邊的子節點則變成父節點
        if largest != index:
            nums[largest], nums[index] = nums[index], nums[largest] #如果原本設定的父節點不是最大的，就互換位置
            self.heapify(nums, largest, size, compare)
            
test = [-1, 4, 5, 6, 0, -4, -1, 7, -3, -2, 2]
Solution().heap_sort(test)
```

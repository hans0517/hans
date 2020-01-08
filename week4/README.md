# QuickSort
* QuickSort(快速排序法):在數列中任意挑選一個數，稱為pivot，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比pivot大」，接著將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，「分別」重複上述步驟(選pivot、調整數列)，直到分不出「新的數列」為止。
## QuickSort流程圖
![image](https://github.com/hans0517/hans/blob/master/week4/QuickSortpic100.png)
## My QuickSort Code
```python
class Solution(object):
    def quicksort(self, list):
        
        left = []
        right = []
        
        if len(list) <= 1:
            return list
        else:
            pivot = list[0]
            while len(list) > 0:
                
                number = list.pop()
                if number > pivot:
                    right.append(number)
                else:
                    left.append(number)
        left = self.quicksort(left)
        right = self.quicksort(right)
        return left +  right
list = [5, -2, 6, -8, -4, 9, 3, 0, 7, -5]
result = Solution().quicksort(list)
print(result)
```
# InsertionSort
* 學習網站 : http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php
* 簡介
  * InsertionSort是將資料分成已排序、未排序兩部份依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置，插入時由右而左比較，直到遇到第一個比正處理的值小的值，再插入，比較時，若遇到的值比正處理的值大或相等，則將值往右移。
* 時間複雜度
  * Best : Ο(1)
    * 當資料的順序恰好為由小到大時，每回合只需比較1次
  * Worst : Ο(n2)
    * 當資料的順序恰好為由大到小時，第i回合需比i次
  * Average : Ο(n2)
    * 第n筆資料，平均比較n/2次
    
![image](https://github.com/hans0517/hans/blob/master/images/Insertion%20Sort.png)
## InsertionSort Code
```python
def insertion_sort(list): #in-place
    for i in range(1, len(list)): #第一個元素固定，從第二個開始
        tmp = list[i]
        #print(tmp)
        j = i - 1 #固定元素的前一個數字
        while j >= 0 and tmp < list[j]:
            list[j + 1] = list[j] #值向右
            j = j - 1
        list[ j + 1 ] = tmp
    return list
nums = [-2, 6, 7, -4, 0, 3, -1, 4]
insertion_sort(nums)
```
# Set Mismatch
## Set Mismatch Code
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        odisum=sum(nums) #原始的加總
        setnums=set(nums) #將nums裡的資料用set整理，set為創建不重複元素的集合
        setsum=sum(setnums) #set後的加總
        a=0
        for i in range(len(nums)+1):
            a = a + i
            repeat = odisum-setsum #用原始的加總扣掉set後的加總就能找出重複的數
            missing = a-setsum
        return repeat, missing
```

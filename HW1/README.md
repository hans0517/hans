# QuickSort
* [學習歷程、流程圖、說明](https://github.com/hans0517/hans/blob/master/HW1/QuickSort%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E8%AA%AA%E6%98%8E.ipynb)
* [Quick Sort程式碼](https://github.com/hans0517/hans/blob/master/HW1/quick_sort_06170234.py)
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

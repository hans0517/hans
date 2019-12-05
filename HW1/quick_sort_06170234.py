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

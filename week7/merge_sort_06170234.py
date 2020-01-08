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

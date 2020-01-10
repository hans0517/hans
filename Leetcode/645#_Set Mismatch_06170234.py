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

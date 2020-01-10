class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)//2):
            now = s[i]
            s[i] = s[-1-i] #第0個值放到最後-1的位置
            s[-1-i] = now #最後一個放在第一個0的位置
        return s #修改完回傳改後之答案

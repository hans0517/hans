class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            xx = str(x)
            if xx == xx[::-1]:
                return True

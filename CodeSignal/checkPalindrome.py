def checkPalindrome(inputString):
    def reverse(inputString):
        return inputString[::-1] #先把inputString轉向
    if inputString == reverse(inputString): #如果轉向完後相等，回傳True，此外則為False
        return True
    else:
        return False

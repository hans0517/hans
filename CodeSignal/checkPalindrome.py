def checkPalindrome(inputString):
    def reverse(inputString):
        return inputString[::-1]
    if inputString == reverse(inputString):
        return True
    else:
        return False

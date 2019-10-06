def adjacentElementsProduct(inputArray):
    abc = [inputArray[i]*inputArray[i+1] #做一個List為前一項和後一項相乘
           for i in range(0, len(inputArray)-1)] #利用迴圈跑完inputArray裡的前一項和後一項相乘
    return max(abc) #回傳題目所需，abc裡的最大值

def quicksort(mylist):
    left = []
    right = []

    if len(mylist) <= 1:
        return mylist

    else:
        pivot = mylist[0] #設第一個數為pivot基準
        for i in mylist:
            if i < pivot: #比基準小的數
                left.append(i)
            elif i > pivot: #比基準大的數
                right.append(i)

    left = quicksort(left)
    right = quicksort(right)
    return left + [pivot] + right
    list = [5, -2, 6, -8, -4, 9, 3, 0, 7, -5]
    result = quicksort(list)
    print('BeforeQuickSort : ' ,list)
    print('AfterQuickSort : ' ,result)

def makeArrayConsecutive2(statues):
    statues = sorted(statues, reverse = False)
    abc = [statues[i+1]-statues[i]-1 for i in range(0, len(statues)-1)]
    return sum(abc)

#program to swap first and last element of a list
#  Swap function
def swapList(newlist) :
    size = len(newlist)

    # Swapping
    temp = newList[0]
    newList [0] = newList[size -1]
    newList[size -1] = temp

    return newlist

    # Driver code
newList = [12, 35, 9, 56, 24]

print (swapList(newList))

"""
The input will start with a positive integer, giving the number
of instances that follow. For each instance,
there will be a string. fOr each string s, the
program should output Hello, s! on its own line.
"""
#number, toSayHello: list


def inversionCount():

    number_inputs = int(input())
    names = []
    for _ in range(number_inputs):
        num_instances = int(input())
        #construct the list:
        raw_list = [int(i) for i in input().split()]
        #start checking inversions
        #this function 
        countTuple = inversionCountHelper(raw_list)
        print(countTuple[1])

def inversionCountHelper(list):
    """
        Input: Comparable List A
        Output: Number of signiicant inversions and sorted array
     """
    if len(list) <= 1:
        return (list, 0)
    else:
        mid = len(list) // 2
        a1c1 = inversionCountHelper(list[:mid])
        a2c2 = inversionCountHelper(list[mid:])
        ac = mergeCount(a1c1[0], a2c2[0])
        return (ac[0], a1c1[1] + a2c2[1] + ac[1])

def mergeCount(list1, list2):
    """
    Input: Two lists of comparable items, A and B
    Output: A merged list and count of inversions
    """
    startingList = []
    count = 0

    # while len(list1) != 0 or len(list2) != 0:
    #     list1Pop = list1.pop(0) #front of A
    #     list2Pop = list2.pop(0) #front of B

    #     #in this case the appended element is from B (B<A)
    #     if (list2Pop < list1Pop):
    #         count += len(list1)
    #         startingList.append(list2Pop)
    #     else:
    #         startingList.append(list1Pop)

    # while list1 and list2:
    #     if list1[0] <= list2[0]:
    #         startingList.append(list1.pop(0))
    #     else:
    #         startingList.append(list2.pop(0))
    #         count += len(list1)   # all remaining elements in list1 are greater
    
    #originally intended to use .pop() but I want to pop the first element not last element
    #pop first element is O(n), which ruins runtime
    #so we use indicies instead of popping.
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            startingList.append(list1[i])
            i += 1
        else:
            startingList.append(list2[j])
            count += len(list1) - i   # all remaining elements in list1 are inversions
            j += 1

    # add leftovers
    startingList.extend(list1[i:])
    startingList.extend(list2[j:])   

    return (startingList, count)
if __name__ == "__main__":
    inversionCount()
def LineIntersection():

    number_inputs = int(input())
    for _ in range(number_inputs):
        num_pairs = int(input())
        #sets up P and Q properly
        P = []
        Q = []
        for _ in range(num_pairs):
            P.append(int(input()))
        for _ in range(num_pairs):
            Q.append(int(input()))

        #Only one pair of points, no intersection
        if num_pairs == 1: print(0)

        print(MergeCountIntersections(P, Q))


def MergeCountIntersections(P, Q):
    #function that finds total number of intersections
    #takes in: pairs P and Q
    #returns: number of intersections

    #if there are
    if len(P) <= 1: return 0

    #there are two or more pairs, divide and conquer
    midpoint = int(len(P) / 2)
    #split the problem in half
    firstPairP, firstPairQ = P[:midpoint], Q[:midpoint]#first half of the pairs
    secondPairP, secondPairQ = P[midpoint:], Q[midpoint:]

    #then merge them
    firstNumIntersections = MergeCountIntersections(firstPairP, firstPairQ)
    secondNumIntersections = MergeCountIntersections(secondPairP, secondPairQ)
    totalNumIntersections = MergeCountPairs(firstPairP, firstPairQ, secondPairP, secondPairQ, firstNumIntersections, secondNumIntersections)

    return totalNumIntersections

def MergeCountPairs(firstPairP, firstPairQ, secondPairP, secondPairQ, firstNumIntersections, secondNumIntersections):
    """
    Uses the merge logic to merge count iterations. Takes in pairs and returns total number
    of new intersections between them
    returns the total number of 
    """
    numNewIntersections = 0
    #xPairP and xPairQ are LISTS of INTEGERS
    for i in range(len(firstPairP)):
        #check any intersections with Ps
        for j in range(len(secondPairP)):
            #check intersections
            numNewIntersections += CheckIntersection(firstPairP[i], firstPairQ[i], secondPairP[j], secondPairQ[j])
    #now we have the new intersections: return the number of total intersections
    return firstNumIntersections + secondNumIntersections + numNewIntersections

def CheckIntersection(p1, p2, q1, q2):
    #returns 1 if intersection exists, 0 otherwise
    if p1 < p2 and q2 < q1:
        return 1
    elif p2 < p1 and q1 < q2:
        return 1
    return 0

if __name__ == "__main__":
    LineIntersection()
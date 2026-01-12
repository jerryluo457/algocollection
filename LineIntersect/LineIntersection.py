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

        # sorts P and Q
        pairs = sorted(zip(P, Q), key=lambda x: x[0])
        P = [p for p, q in pairs]
        Q = [q for p, q in pairs]

        #only one pair of points, no intersection
        if num_pairs == 1:
            print(0)
            continue
        
        #use mergesort logic to count number of intersections
        # Replace the previous D&C merge logic with a direct inversion count on Q
        print(CountInversions(Q))


def CountInversions(arr):
    """
    Count inversions in arr using merge sort.
    Returns the inversion count (int). 
    """
    if not arr: #empty arr, nothing to count
        return 0
    # work on a copy to avoid surprising caller-side mutations
    a = list(arr)
    temp = [0] * len(a)
    return MergeCount(a, temp, 0, len(a) - 1)


def MergeCount(a, temp, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    inv = MergeCount(a, temp, left, mid)
    inv += MergeCount(a, temp, mid + 1, right)

    # merge step: count cross inversions
    i = left       # pointer into left half
    j = mid + 1    # pointer into right half
    k = left       # pointer into temp
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            # a[i] > a[j] => all remaining a[i..mid] are inversions against a[j]
            temp[k] = a[j]
            inv += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = a[j]
        j += 1
        k += 1

    # copy back
    for idx in range(left, right + 1):
        a[idx] = temp[idx]
    return inv


# check sintersections
def CheckIntersection(p1, p2, q1, q2):
    #returns 1 if intersection exists, 0 otherwise
    if p1 < p2 and q2 < q1:
        return 1
    elif p2 < p1 and q1 < q2:
        return 1
    return 0


if __name__ == "__main__":
    LineIntersection()

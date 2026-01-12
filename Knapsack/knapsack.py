def knapsack():
    number_inputs = int(input())

    for _ in range(number_inputs):
        #implement algorithm. We have to find the number of items that follow
        #as well as the capacity of the knapsack
        header = input().split()
        numItems = int(header[0])
        capacity = int(header[1])

        items = [] #a list of lists [[w1, v1], [w2, v2], [w3, v3]]

        for i in range(numItems):
            int_list = [int(value) for value in input().split()]
            items.append(int_list)

        #construct the DP array DP[i][j] 
        #is the max value of stolen goods picking from 
        #the ith index while constrained by capacity of j
        DPArray = [[0 for _ in range(capacity + 1)] for _ in range(numItems + 1)]
        
        for item in range(1, numItems + 1):
            for weightRemaining in range(capacity + 1):
                if items[item - 1][0] > weightRemaining:
                    DPArray[item][weightRemaining] = DPArray[item - 1][weightRemaining]
                else:
                    DPArray[item][weightRemaining] = max(
                        DPArray[item - 1][weightRemaining], #not include
                        DPArray[item - 1][weightRemaining - items[item - 1][0]] + items[item - 1][1] #include
                    )
        
        # print(DPArray)
        print(DPArray[numItems][capacity])
if __name__ == "__main__":
    knapsack()

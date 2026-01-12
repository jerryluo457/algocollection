"""
Performs a depth first traversal
"""
#number, toSayHello: list


def DFS():

    num_instances = int(input())
    for instance in range(num_instances):

        num_nodes = int(input())
        inGraph = []

        for _ in range(num_nodes):
            inGraph.append(input())

        #Turn the input into a 2D array
        visited = []
        nodePositions = {}
        graphArray = []
        # print(len(names))
        
        for i in range(num_nodes):
            toAdd = inGraph[i].strip().split(" ")
            graphArray.append(toAdd) #O(n)
            nodePositions[toAdd[0]] = i

        print(f"instance {instance, graphArray}")
        # print(nodePositions)

        j = 0 #current node index
        for j in range(num_nodes): 
            if (graphArray[j][0] not in visited):
                visited.append(graphArray[j][0])
                print(visited)
                #set j next on list that is not visited
                print(f"length of graph array for the line",len(graphArray[j]))
                for k in range(len(graphArray[j])):
                    print(f"k is", {k})
                    if graphArray[j][k] not in visited:
                        print(f"*** is", graphArray[j][k])
                        visited.append(graphArray[j][k])
                        print(f"j is", {j}, "k is", {k})
                        print(nodePositions[graphArray[j][k]])
                        j = int(nodePositions[graphArray[j][k]])
                        print(f"j is", {j})
                        k = 0
                        break
                    #if there is none that is not visited, go to the next line 
                    elif k == (len(graphArray[j]) - 1) and graphArray[j][k] not in visited:
                        j+=1
                        k = 0
                        break
                
                # for k in range(len(graphArray[j])):
                #     print(f"k is {k}")
                #     if graphArray[j][k] not in visited:
                #         print(f"*** is", graphArray[j][k])
                #         j = int(nodePositions[graphArray[j][k]])
                #         # break out, because 'j' has changed
                #         break
                #     elif k == (len(graphArray[j]) - 1) and graphArray[j][k] not in visited:
                #         j += 1
                #         break

        print("visited is: ")
        print(visited)

    
if __name__ == "__main__":
    DFS()
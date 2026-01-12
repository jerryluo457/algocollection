def DFS():
    num_instances = int(input())
    # will be many graph instances in the input
    for _ in range(num_instances):
        # multiple numbers of nodes for each instance
        num_nodes = int(input())
        inGraph = [] 
        for _ in range(num_nodes): 
            inGraph.append(input())

        # produce 2d array modeling graph
        graphArray = [] 
        for i in range(num_nodes): 
            toAdd = inGraph[i].strip().split() 
            # print(toAdd)
            graphArray.append(toAdd) #O(n) nodePositions[toAdd[0]] = i

        # creates adj dictionary so we can easily look up different things
        graph = {}
        for row in graphArray:
            # print(neighbors)
            # print(row)
            graph[row[0]] = [] if len(row) == 1 else row[1:]  #node is first element of array, neighbours second
        
        # print(graph)
        # track visited nodes so we can print them out as required
        visited = []

        # recursive DFS
        def dfs(node):
            if node in visited: #already visited
                return
            visited.append(node)  # mark as visited
            # explore all neighbors in the order given in input
            for neighbor in graph.get(node, []):
                dfs(neighbor)

        # if graph is disconnected, like C, go to next row
        for row in inGraph:
            node = row.strip().split()[0]
            # print(row)
            # print(f"row 0 is", row[0])
            # print(f"improved version is", row.strip().split()[0])
            if node not in visited:
                dfs(node)

        # Print the traversal order for this graph instance
        print(" ".join(visited))


if __name__ == "__main__":
    DFS()

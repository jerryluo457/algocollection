from collections import defaultdict, deque

class Network:
    # graph data structure to support flow algorithms.
    #  edgeList format: [[inLabel, outLabel, capacity], ...]
    def __init__(self, edgeList):
        # store Node objects by label
        self.nodes = {}
        # store list of Edge objects
        self.edges = []
        # adjacency list: label -> list of (neighbor_label, capacity)
        self.adj = defaultdict(dict)
        # for find_bottleneck compatibility (residual graph)
        self.graph = defaultdict(dict)

        for inLabel, outLabel, capacity in edgeList:
            # create nodes if they don't exist
            if inLabel not in self.nodes:
                self.nodes[inLabel] = Node(inLabel)
            if outLabel not in self.nodes:
                self.nodes[outLabel] = Node(outLabel)

            # create the edge
            edge = Edge(self.nodes[inLabel], self.nodes[outLabel], capacity)
            self.edges.append(edge)

            # store in adjacency list (directed)
            # sum capacities for parallel edges instead of overwriting
            self.adj[inLabel][outLabel] = self.adj[inLabel].get(outLabel, 0) + capacity

            # used for residual graph: also sum parallel edges
            self.graph[inLabel][outLabel] = self.graph[inLabel].get(outLabel, 0) + capacity

            # ensure reverse edge exists with 0 capacity
            self.graph[outLabel].setdefault(inLabel, 0)
            self.adj[outLabel].setdefault(inLabel, 0)

    def getNodes(self):
        return list(self.nodes.values())

    def getEdges(self):
        return self.edges

    def getNeighbors(self, label):
        # return all neighbors of a node (labels).
        return list(self.graph[label].keys())

    def bfs(self, source, sink):
        # Example BFS (returns parent map if path exists, else None).
        visited = set()
        parent = {}
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            for v, capacity in self.graph[u].items():
                # use residual graph
                if v not in visited and capacity > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return parent
                    queue.append(v)
        return None  # no path found

    def find_bottleneck(self, source, sink, parent, update=False):
        # find bottleneck and update residual graph
        bottleneck = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            bottleneck = min(bottleneck, self.graph[u][v])
            v = u

        if update:
            v = sink
            while v != source:
                u = parent[v]
                # reduce forward capacity
                self.graph[u][v] -= bottleneck
                # increase reverse capacity (ensure key exists then add)
                self.graph[v][u] = self.graph[v].get(u, 0) + bottleneck
                v = u

        return bottleneck

    def __repr__(self):
        desc = []
        for u in self.graph:
            for v, cap in self.graph[u].items():
                if cap > 0:
                    desc.append(f"{u} -> {v} (cap={cap})")
        return "Network:\n" + "\n".join(desc)


class Node:
    def __init__(self, label):
        self.label = label

    def getLabel(self):
        return self.label


class Edge:
    def __init__(self, in_Node, out_Node, value):
        self.inNode = in_Node
        self.outNode = out_Node
        self.value = value

    def getInNode(self):
        return self.inNode

    def getOutNode(self):
        return self.outNode

    def getVal(self):
        return self.value


def run_NF(string):
    # handle string input properly
    lines = [line.strip() for line in string.splitlines() if line.strip()]  
    indx = 0
    number_inputs = int(lines[indx])  
    indx += 1
    for _ in range(number_inputs):
        nodes, edges = [int(i) for i in lines[indx].split()] 
        indx += 1
        edgeList = []
        for _ in range(edges):
            u, v, cap = lines[indx].split()  
            indx += 1
            # FIX: allow string nodes like 's' and 't'
            try:
                u = int(u)
            except:
                pass
            try:
                v = int(v)
            except:
                pass
            edgeList.append([u, v, int(cap)])
        network = Network(edgeList)
        #start network
        source = 's' 
        sink = 't'  

        # FF loop
        max_flow = 0
        while True:
            parent = network.bfs(source, sink)
            if not parent:
                break  # no more augmenting paths
            bottleneck = network.find_bottleneck(source, sink, parent, update=True)
            max_flow += bottleneck
        return max_flow


def find_source(edges):
    non_source = set([i[1] for i in edges])
    return list({i[0] for i in edges} - {i[1] for i in edges})[0]


def find_sink(edges):
    return list({i[1] for i in edges} - {i[0] for i in edges})[0]


def main():
    number_inputs = int(input())
    for _ in range(number_inputs):
        # FIX: move string_out inside loop
        string_out = []  # <-- FIX
        string_out.append("1")  # one instance per run_NF
        #this is each instance
        #we first construct the graph, then find the max flow.
        meta = input().split()
        num_A = int(meta[0])
        num_B = int(meta[1])
        edges = int(meta[2])
        num_nodes = num_A + num_B + 2
        temp = []
        num_edge = 0
        for i in range(edges):
            #connect s to first element of edge
            #connect second element of edge to t
            #connect edges to each other
            ab = input().split()
            a = int(ab[0])
            b = int(ab[1])
            # --- FIX: map B-side labels so they don't collide with A-side labels ---
            b_mapped = num_A + b
            if (f"s {a} 1" not in temp):
                temp.append(f"s {a} 1")  #connect s to a
                num_edge += 1
            if (f"{b_mapped} t 1" not in temp):
                temp.append(f"{b_mapped} t 1")  #connect b to t (mapped)
                num_edge += 1
            temp.append(f"{a} {b_mapped} 1")  #connect a with mapped b
            num_edge += 1
        #finished with that instance, we know what the edge is
        string_out.append(f"{num_nodes} {num_edge}")
        string_out.extend(temp)
        temp.clear()
        #construct the input string to put into last week's implementation.
        str_final = "\n".join(str(line).strip() for line in string_out if line)  
        max_flow = run_NF(str_final)
        #apply therom 
        if max_flow >= max(num_A, num_B):  
            print(f"{max_flow} Y")
        else:
            print(f"{max_flow} N")


if __name__ == "__main__":
    main()

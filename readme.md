# Algorithm Implementations Collection

A comprehensive collection of fundamental algorithms implemented in C. This repository covers graph theory, greedy strategies, dynamic programming, and advanced network analysis.

## Algorithms Included

### 1. Graph Algorithms
* **Depth-First Search (DFS):** A recursive approach to exploring graph nodes and edges. Useful for connectivity testing and topological sorting.
* **Network Flow (Max-Flow):** Implementation of flow networks (e.g., Edmonds-Karp or Ford-Fulkerson) to find the maximum possible flow from a source to a sink.


### 2. Scheduling & Greedy Strategies
* **Finish First Scheduling:** A greedy approach to the Interval Scheduling problem that maximizes the number of non-overlapping tasks by always picking the one that finishes earliest.
* **Interval Scheduling:** Logic for managing resources and time-slots to prevent overlaps in task execution.

### 3. Divide and Conquer
* **Inversion Count:** An efficient $O(n \log n)$ algorithm (based on Merge Sort) used to count how far an array is from being sorted.
* **Divide and Conquer Frameworks:** General implementations of recursive problem-solving that break problems into smaller sub-problems.


### 4. Dynamic Programming
* **0/1 Knapsack Problem:** An optimization algorithm that selects items with specific weights and values to maximize total value without exceeding a weight capacity.


---

## Compilation and Usage

Most implementations can be compiled using makefile. For example:

```bash
# Compile a specific algorithm
make run

'''
Certainly! The provided Python code implements Dijkstra's algorithm for finding the shortest path in a weighted graph. Let's go through the code step by step:

1. Graph Representation: The code starts by defining a graph using a dictionary data structure. The keys of the dictionary represent the nodes of the graph, and the values are dictionaries that map neighboring nodes to their corresponding edge weights. This representation allows efficient access to the neighbors and weights of each node.

2. Dijkstra's Algorithm Implementation: The code defines a function named `dijkstra` that takes the graph and a starting node as input parameters.

   - Initialization: The function initializes the `distances` dictionary, which stores the shortest distances from the starting node to each node in the graph. Initially, all distances are set to infinity except for the starting node, which is set to 0. The `previous` dictionary is also initialized to keep track of the previous node in the shortest path.

   - Priority Queue: The function uses a priority queue, implemented as a heap, to efficiently select the node with the smallest distance. The `queue` variable is a list of tuples, where each tuple contains the distance and the node. The starting node is added to the queue with a distance of 0.

   - Dijkstra's Algorithm Loop: The main loop of Dijkstra's algorithm continues until the queue is empty.

     - Selecting the Node: In each iteration, the node with the smallest distance is popped from the queue using `heapq.heappop(queue)`. The `heapq` module provides functions for working with heaps.

     - Relaxation: For each neighboring node of the current node, the algorithm checks if the distance to reach that node through the current node is shorter than the current known distance. If so, the distance is updated, the previous node is set to the current node, and the neighboring node is added to the queue with the updated distance.

   - Return Values: After the algorithm completes, the function returns the `distances` dictionary, which contains the shortest distances from the starting node to each node in the graph, and the `previous` dictionary, which contains the previous node in the shortest path.

3. Driver Code: The code calls the `dijkstra` function with the given graph and starting node 'A'. The returned `Node_distance` dictionary contains the shortest distances from node 'A' to each node, and the `Path` dictionary contains the previous node in the shortest path.

4. Output: The code prints the `Node_distance` and `Path` dictionaries, which represent the shortest distances and paths from the starting node 'A' to each node in the graph, respectively.

The code effectively applies Dijkstra's algorithm to find the shortest path in a weighted graph, considering positive edge weights.
'''
graph={
    'A':{'B':2,'C':3},
    'B':{'D':3,'E':1},
    'C':{'F':2},
    'D':{},
    'E':{'F':1},
    'F':{}
	}

import heapq
def dijkstra(graph,node):
	distances={node:float('inf') for node in graph}
	print("distances::",distances)
	distances[node]=0
	previous={node:None for node in graph}
	queue=[(0,node)]
	print("Value of QUEUE ==> ",queue)
	
	while queue:
		current_distance,current_node=heapq.heappop(queue)
		print("Cureent Distance and Node ==> ",current_distance)
		print("Cureent Node ==> ",current_node)
		# relaxation
		for next_node,weight in graph[current_node].items():
			distance_temp=current_distance+weight
			if distance_temp<distances[next_node]:
				distances[next_node]=distance_temp
				previous[next_node]=current_node
				heapq.heappush(queue,(distance_temp,next_node))
			print("Distances::",distances)
	return distances,previous

#Driver Code
Node_distance, Path = dijkstra(graph,'A')
print(Node_distance)
print(Path)

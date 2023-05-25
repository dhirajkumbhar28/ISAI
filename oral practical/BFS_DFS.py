'''
Certainly! The provided Python code implements breadth-first search (BFS) and depth-first search (DFS) algorithms on a graph. Let's go through the code step by step:

1. `graph`: This is a dictionary representing the graph. Each key in the dictionary represents a node, and the corresponding value is a list of neighboring nodes.

2. `visited` and `queue`: These are lists used to keep track of visited nodes and to store nodes to be processed in BFS.

3. `bfs(visited, graph, node)`: This function implements breadth-first search. It takes the `visited` list, the `graph`, and a starting `node` as input. It starts by adding the starting node to the visited list and the queue. Then it iterates until the queue is empty. In each iteration, it removes the first node from the queue (`m`), prints it, and adds its unvisited neighbors to the visited list and the queue.

4. `visited1`: This is a set used to keep track of visited nodes in DFS.

5. `dfs(visited1, graph, node)`: This function implements depth-first search. It takes the `visited1` set, the `graph`, and a starting `node` as input. It checks if the current node is already visited. If not, it prints the node, adds it to the visited set, and recursively calls the `dfs` function for each unvisited neighbor.

6. The main part of the code uses a while loop to repeatedly prompt the user for a choice: BFS, DFS, or Exit. Depending on the choice, it calls the respective search function (`bfs` or `dfs`) with the provided graph and starting node ('5'). After executing the chosen search algorithm, it asks the user if they want to continue or exit the program.

Overall, this code provides a simple menu-driven program to perform BFS and DFS on the given graph. It allows the user to choose between BFS and DFS, displays the search results, and provides an option to continue or exit the program.
'''
graph = {'5': ['3', '7'], '3': ['2', '4'],'7': ['8'], '2': [], '4': ['8'], '8': []}
visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end="\n")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


visited1 = set()
def dfs(visited1, graph, node):
    if node not in visited1:
        print(node)
        visited1.add(node)
        for neighbour in graph[node]:
            dfs(visited1, graph, neighbour)


flag = 1
while flag == 1:
    print("1. BFS \n 2. DFS \n 3. Exit \n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("Following is the BFS:")
        bfs(visited, graph, '5')
        a = input("Do you want to continue(y/n): ")
        if a == "y":
            flag = 1
        else:
            flag = 0
    elif ch == 2:
        print("Following is the BFS:")
        dfs(visited1, graph, '5')
        a = input("Do you want to continue(y/n): ")
        if a == "y":
            flag = 1
        else:
            flag = 0
    elif ch == 3:
            flag = 0
            print("Thanks for using this program")
    else:
        print("Wrong choice")
        a = input("Do you want to continue(y/n):")
        if a == "y":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program")

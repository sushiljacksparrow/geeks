class adj_node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        # create destination node and add src to destination node
        node = adj_node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # this should only be enabled if graph is not directed
        # node = adj_node(src)
        # node.next = self.graph[dest]
        # self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end = "")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end ="")
                temp = temp.next
            print(" \n")

    def bfs(self, s):
        visited = [False] * (self.V)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s)

            temp = self.graph[s]
            while temp:
                if visited[temp.vertex] == False:
                    queue.append(temp.vertex)
                    visited[temp.vertex] = True
                temp = temp.next

    def dfs(self, s, visited):
        stack = []
        stack.append(s)
        while stack:
            s = stack.pop()
            print(s)

            temp = self.graph[s]
            while temp:
                if visited[temp.vertex] == False:
                    visited[temp.vertex] = True
                    stack.append(temp.vertex)
                temp = temp.next

    def topological_sort_util(self, s, visited, stack):
        visited[s] = True
        temp = self.graph[s]
        while temp:
            if visited[temp.vertex] == False:
                self.topological_sort_util(temp.vertex, visited, stack)
            temp = temp.next
        stack.insert(0, s)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        print(stack)

if __name__ == "__main__":
    V = 6
    graph = Graph(V)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(4, 1)
    graph.add_edge(4, 0)
    graph.add_edge(5, 0)
    graph.add_edge(5, 2)
    # graph.add_edge(3, 4)

    # graph.print_graph()

    # graph.bfs(2)
    visited = [False] * V

    # for i in range(len(visited)):
    #     if visited[i] == False:
    #         visited[i] = True
    #         graph.dfs(i, visited)

    graph.topological_sort()

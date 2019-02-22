class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, V, set):
        self.V = V
        self.graph = [None] * self.V
        self.dict = {}
        self.reverse_dict = {}
        for i in range(len(set)):
            print(set[i], i)
            self.dict[set[i]] = i
            self.reverse_dict[i] = set[i]

    def add_edge(self, source, dest):
        node = Node(dest)
        node.next = self.graph[self.dict[source]]
        self.graph[self.dict[source]] = node

    def print(self):
        for i in range(self.V):
            print("Adjacency list from vertext with head {}".format(self.reverse_dict[i]), end="")
            temp = self.graph[i]
            while temp:
                print(" --> {} ".format(temp.data), end="")
                temp = temp.next
            print(" \n")

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        temp = self.graph[v]
        while temp:
            if visited[self.dict[temp.data]] == False:
                self.topological_sort_util(self.dict[temp.data], visited, stack)
            temp = temp.next
        stack.insert(0, self.reverse_dict[v])

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        print(stack)

if __name__ == "__main__":


    # V = 6
    # graph = Graph(V)
    # graph.add_edge(2, 3)
    # graph.add_edge(3, 1)
    # graph.add_edge(4, 1)
    # graph.add_edge(4, 0)
    # graph.add_edge(5, 0)
    # graph.add_edge(5, 2)

    # words = ["baa", "abcd", "abca", "cab", "cad"]

    words = ["caa", "aaa", "aab"]

    set = []
    for word in words:
        for c in word:
            if c not in set:
                set.append(c)

    V = len(set)


    graph = Graph(V, set)
    for i in range(len(words)-1):
        first = words[i]
        second = words[i+1]
        for c1 in range(len(first)):
            for c2 in range(len(second)):
                if first[c1] != second[c2]:
                    graph.add_edge(first[c1], second[c2])



    graph.print()

    graph.topological_sort()

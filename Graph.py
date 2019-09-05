#  File: Graph.py
#  Description: this program models and simulates graph traversals

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 08/08/2019
#  Date Last Modified: 08/09/2019

class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return (self.queue.pop(0))

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).label):
                return True
        return False

    # given a label get the index of a vertex
    def get_index(self, vertex_label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.Vertices[i]).label == vertex_label:
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if not self.has_vertex(label):
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix for the new Vertex
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new Vertex in the adjacency matrix
            new_row = []
            for i in range(nVert):
                new_row.append(0)
            self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # return edge weight of edge starting at from_vertex_label
    # and ending at to_vertex_label
    # from_vertex_label and to_vertex_label are strings
    # returns an integer
    # return -1 if edge does not exist
    def get_edge_weight(self, from_vertex_label, to_vertex_label):
        from_vertex_index = self.get_index(from_vertex_label)
        to_vertex_index = self.get_index(to_vertex_label)
        if self.adjMat[from_vertex_index][to_vertex_index] != 0:
            return self.adjMat[from_vertex_index][to_vertex_index]
        return -1

    # return a list of indices of immediate neighbors that
    # you can reach from the vertex with the given label
    # vertex_label is a string and the function returns a list of integers
    # return empty list if there are none or if the given label is not
    # in the graph
    def get_neighbors(self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        neighbors = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[vertex_index][i] > 0:
                neighbors.append(i)
        return neighbors

    # return a list of the vertices in the graph
    # returns a list of Vertex objects
    def get_vertices(self):
        return self.Vertices

    # delete an edge from the graph
    # from_vertex_label and to_vertex_label are strings
    # if there is no edge, does nothing
    # does not return anything
    # make sure to modify the adjacency matrix appropriately
    def delete_edge(self, from_vertex_label, to_vertex_label):
        from_vertex_index = self.get_index(from_vertex_label)
        to_vertex_index = self.get_index(to_vertex_label)
        self.adjMat[from_vertex_index][to_vertex_index] = 0

    # delete a vertex from the graph
    # vertex_label is a string
    # if there is no such vertex, does nothing
    # does not return anything
    # make sure to remove vertex from vertex list AND
    # remove the appropriate row/column of the adjacency matrix
    def delete_vertex(self, vertex_label):
        if self.has_vertex(vertex_label):
            vertex_index = self.get_index(vertex_label)
            self.Vertices.pop(vertex_index)

            # delete the column of the vertex
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                self.adjMat[i].pop(vertex_index)

            # delete the row of the vertex
            self.adjMat.pop(vertex_index)

    # do the depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit other vertices according to depth
        while (not theStack.isEmpty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the depth first search in a graph
    def bfs(self, v):
        # create the Queue:
        theQueue = Queue()

        # mark vertex v as visited
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # visit an adjacent unvisited vertex in order from the current vertex
        # mark it visited and insert it into the Queue
        while not theQueue.isEmpty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theQueue.peek())
            if u == -1:
                u = theQueue.dequeue()
            else:
                self.Vertices[u].visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)

        # the Queue is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False


def main():
    # create a Graph object
    cities = Graph()

    # open file for reading
    in_file = open("./graph.txt", "r")

    # read the Vertices
    num_vertices = int((in_file.readline()).strip())
    print(num_vertices)

    for i in range(num_vertices):
        city = (in_file.readline()).strip()
        print(city)
        cities.add_vertex(city)

    # read the edges
    num_edges = int((in_file.readline()).strip())
    print(num_edges)

    for i in range(num_edges):
        edge = (in_file.readline()).strip()
        print(edge)
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # print the adjacency matrix
    print("\nAdjacency Matrix")
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(cities.adjMat[i][j], end=' ')
        print()
    print()

    # read the starting vertex for dfs and bfs
    start_vertex = (in_file.readline()).strip()
    print(start_vertex)

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)
    print(start_index)

    # test depth first search
    print("\nDepth First Search from " + start_vertex)
    cities.dfs(start_index)
    print()

    # test breadth first search
    print("\nBreath First Search from " + start_vertex)
    cities.bfs(start_index)
    print()

    # test deletion of an edge
    cities.delete_edge("Seattle", "San Francisco")
    print()

    # test deletion of a vertex
    cities.delete_vertex("Houston")
    num_vertices = num_vertices - 1
    print()

    # new AdjMat
    print("\nAdjacency Matrix")
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(cities.adjMat[i][j], end=' ')
        print()
    print()

    # close the file
    in_file.close()


main()


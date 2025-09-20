import random

class simpleGraph:
    def __init__(self):
        self.graph = {}
        """
        key of dict as point (eg. a,b,c) and value as a set consisting of the 
        neighbours
        example:
        {
        A : (C, D),
        C : (A, D),
        D : (C, A),
        B : ()
        }
        """

    def addVertex(self, u):
        if not u in self.graph:
            self.graph[u] = set()
    
    def addEdge(self, u, b):
        if u in self.graph and b in self.graph:
            self.graph[u].add(b)
            self.graph[b].add(u)
        else:
            print("at least one vertex doesnt exist")

    def deg(self, u):
        if u in self.graph:
            return len(self.graph[u])
        else:
            print('Vertex not found')

    def connectedGraph(self): 
        """
        while not all neighbours(the queue) are visited, 
        we go to all the neighbours and set them as visited 
        and then we add their neighbors to the queue
        """

        if not self.graph:
            return

        start = next(iter(self.graph))
        queue = [start] # first element of graph
        visited = {start}

        while queue:
            node = queue.pop(0) #random elemet (can take random because eventually we will have taken all of the nodes)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)    #add neighbours to queue

                    visited.add(neighbour)  #add element to visited

        return len(visited) == len(self.graph) 

    def connectedComponents(self):
        if not self.graph:
            return []
        # declare variables
        visited = set()
        components = []

        for node in self.graph: #check every node
            if node not in visited: #if node not yet visited
                #declare variables for current connectedGraph
                queue = [node]              
                component_nodes = {node}
                visited.add(node)

                while queue:
                    current = queue.pop(0) #chose random node
                    for neighbour in self.graph[current]: #check all the neighbours
                        if neighbour not in visited:
                            visited.add(neighbour)
                            component_nodes.add(neighbour)
                            queue.append(neighbour)

                components.append(component_nodes)

        return components

    def randomGraph(self, numVertices, edgeProb):

        for i in range(numVertices):
            self.addVertex(str(i))
        
        vertices = list(self.graph.keys())
        for i in range(numVertices):
            for j in range(i + 1, numVertices):
                if random.random() < edgeProb:
                    self.addEdge(vertices[i], vertices[j])




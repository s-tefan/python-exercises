class WGraph:
    def __init__(self):
        nodes = set()
        edges = set()

    def add_edge(self, fromV, toV, weight):
        self.nodes.update({fromV,toV})
        self.edges.add((fromV,toV,weight))
    
    def dijkstra(self, start):
        nodes_unvisited = \
            {[node, math.inf] for node in self.nodes}
        current = [start, 0]
        nodes_unvisited.remove(start) # will raise error if start not in graph

        pass # Här blir det att fortsätta




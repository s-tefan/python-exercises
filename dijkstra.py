class WGraph:
    def __init__(self):
        nodes = set({})
        edges = set({})

    def add_edge(self, fromV, toV, weight):
        self.nodes.update({fromV,toV})
        self.edges.add((fromV,toV,weight))
    
    def dijkstra(self, start):
        nodescopy = self.nodes.copy()
        nodescopy.remove(start)
        nodelist = [start] + nodescopy
        pass # Här blir det att fortsätta




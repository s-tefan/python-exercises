class Tree:
    pass

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

    def add_child(self, child):
        self.children += child


    def breadth(self):
        nextlevel = []
        values = [self.value]
        for c in self.children:
            values.append(c.value)
            nextlevel += c.children
        if nextlevel:
            for n in nextlevel:
                values += n.breadth()
            return values
        else:
            return values

    def depth(self):
        values = [self.value]
        for c in self.children:
            values += c.depth()
        return values


if __name__ == '__main__':
    sum1 = Node('+', [Node('a',[]), Node('b',[])])
    sum2 = Node('+', [Node('c',[]), Node('d',[])])
    prod1 = Node('*', [sum1, sum2])
    print(prod1.breadth())    
    print(prod1.depth())    
    

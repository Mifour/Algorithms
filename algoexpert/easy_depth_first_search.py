class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		array.append(self.name)
		for todo in self.children:
			todo.depthFirstSearch(array)
		return array

class Tree:
        def __init__(self, val, children=[]):
                self.val=val
                self.children = children

def print_tree(tree):
        """
        print a tree level by level with unlimited children nodes in zig zag maneer
        O(n) time
        O(n) space
        """
        way = -1
        list_nodes = []
        next_nodes = []
        list_nodes.append(tree)
        while list_nodes:
                if way == 1:
                        to_join = [str(node.val) for node in list_nodes]
                else:
                        to_join = [str(node.val) for node in list_nodes][-1::-1]
                way*=-1
                print(''.join(to_join))
                index = len(list_nodes)
                for node in list_nodes:
                        for child in node.children:
                                next_nodes.append(child)
                list_nodes = next_nodes
                next_nodes = []

a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)] )] )

print(print_tree(a))
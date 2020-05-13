# 1 Binary tree
# A class that represents an individual node in a Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# create root
root = Node(1)
root.left = Node(2);
root.right = Node(3);
root.left.left  = Node(4);
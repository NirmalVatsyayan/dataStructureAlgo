#level order traversal of Binary Tree
 
# A node structure
class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None
 
 
# Function to  print level order traversal of tree
def printSpiralLevelOrder(root):
    h = height(root)
    print("Height calculated -> ", h)
    forward = False
    for i in range(1, h+1):
        printGivenLevel(root, i, forward)
        forward = not forward
 
 
# Print nodes at a given level
def printGivenLevel(root , level, forward):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1 :
        if forward:
            printGivenLevel(root.left , level-1, forward)
            printGivenLevel(root.right , level-1, forward)
        else:
            printGivenLevel(root.right , level-1, forward)
            printGivenLevel(root.left , level-1, forward)
 
 
""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree 
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(7)
root.left.right = Node(6)

root.right.left = Node(5)
root.right.right = Node(4)
 
print("Level order traversal of binary tree is -> ")
printSpiralLevelOrder(root)

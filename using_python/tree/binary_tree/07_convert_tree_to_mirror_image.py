# Python program to convert a tree to mirror image
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A function to do inorder tree traversal
def printInorder(root):
    if root: 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.data)
 
        # now recur on right child
        printInorder(root.right)

def mirror(root):
    if root == None:
        return
    else:
        mirror(root.left)
        mirror(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Inorder traversal of binary tree is")
printInorder(root)

mirror(root)

print("\n\nInorder traversal of mirror binary tree is")
printInorder(root)

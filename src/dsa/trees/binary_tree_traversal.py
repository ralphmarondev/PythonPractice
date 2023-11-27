class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


'''
In inorder traversal, the left subtree is traversed first,
followed by visiting the current node, and then traversing 
the right subtree.
'''


def inorder_traversal(node):
    if node is None:
        return
    # traverse left subtree
    inorder_traversal(node.left)
    print(node.data, end=' ')  # process current node
    inorder_traversal(node.right)  # traverse right subtree


'''
In preorder traversal, the current node is visited first, 
followed by traversing the left subtree and then the 
right subtree.
'''
def preorder_traversal(node):
    if node is None:
        return

    print(node.data, end=' ')  # process current node
    preorder_traversal(node.left)  # traverse left subtree
    preorder_traversal(node.right)  # traverse right subtree


'''
In postorder traversal, the left subtree is traversed first, 
followed by traversing the right subtree, and finally 
visiting the current node.
'''
def postorder_traversal(node):
    if node is None:
        return

    postorder_traversal(node.left) # traverse left subtree
    postorder_traversal(node.right) # traverse right subtree
    print(node.data, end=' ') # process current node


if __name__ == '__main__':
    # construct a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # perform inorder traversal on the binary tree
    print("Inorder traversal: ", end='')
    inorder_traversal(root)
    print()

    print("Preorder traversal: ", end='')
    preorder_traversal(root)
    print()

    print("Postorder traversal: ", end='')
    postorder_traversal(root)
    print()

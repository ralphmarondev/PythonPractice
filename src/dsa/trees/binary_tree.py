class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children, get the inorder successor
            # (smallest in the right subtree)
            root.key = self._min_value_node(root.right).key

            # delete the inorder successor
            root.right = self._delete(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left
        return current


if __name__ == '__main__':
    bst = BST()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(f"Inorder traversal: {bst.inorder_traversal()}")

    # search for a key
    search_key = 4
    result = bst.search(search_key)

    if result:
        print(f"Key {search_key} found in the tree")
    else:
        print(f"Key {search_key} not found in the tree")

    # delete a key
    delete_key = 3
    bst.delete(delete_key)
    print(f"Key {delete_key} deleted from the tree.")

    print(f"Inroder traversal after deletion: {bst.inorder_traversal()}")

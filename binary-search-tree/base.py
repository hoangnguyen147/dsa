class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, key):
        current = self.root
        while current:
            if current.val == key:
                return True
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.val

    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.val
    
    def left_most_node(current):
        while current.left:
            current = current.left
        return current

    def remove(self, key):
        if self.root is None:
            return False
        current = self.root
        if current.val == key:
            if current.left is None and current.right is None:
                self.root = None
                return True
            elif current.left is None:
                self.root = current.right
                return True
            elif current.right is None:
                self.root = current.left
                return True
            else:
                successor_parent = current
                successor = current.right
                while successor.left:
                    successor_parent = successor
                    successor = successor.left
                current.val = successor.val
                if successor == successor_parent.left:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
                return True
            
        parent = None
        while current:
            if key < current.val:
                parent = current
                current = current.left
            elif key > current.val:
                parent = current
                current = current.right
            else:
                if current.left is None and current.right is None:
                    if current == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                elif current.left is None:
                    if current == parent.left:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    if current == parent.left:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    successor_parent = current
                    successor = current.right
                    while successor.left:
                        successor_parent = successor
                        successor = successor.left
                    current.val = successor.val
                    if successor == successor_parent.left:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                return True
        return False

    def preorder_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                result.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
        return result

    def inorder_traversal(self):
        result = []
        stack = []
        current = self.root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right
        return result

    def postorder_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                result.append(current.val)
                stack.append(current.left)
                stack.append(current.right)
        return result[::-1]

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    assert bst.preorder_traversal() == [50, 30, 20, 40, 70, 60, 80]
    assert bst.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]
    assert bst.postorder_traversal() == [20, 40, 30, 60, 80, 70, 50]

    assert bst.find_max() == 80
    assert bst.find_min() == 20
    assert bst.search(30) == True
    assert bst.search(20) == True
    assert bst.search(80) == True
    assert bst.search(10) == False
    assert bst.search(-10) == False

    assert bst.remove(30) == True
    assert bst.preorder_traversal() == [50, 40, 20, 70, 60, 80]
    assert bst.inorder_traversal() == [20, 40, 50, 60, 70, 80]
    assert bst.postorder_traversal() == [20, 40, 60, 80, 70, 50]

    assert bst.remove(10) == False
    bst.insert(30)
    assert bst.preorder_traversal() == [50, 40, 20, 30, 70, 60, 80]
    assert bst.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]
    assert bst.postorder_traversal() == [30, 20, 40, 60, 80, 70, 50]

    assert bst.remove(30) == True
    assert bst.remove(80) == True
    assert bst.remove(20) == True
    assert bst.remove(50) == True
    assert bst.remove(60) == True
    assert bst.remove(70) == True
    assert bst.remove(40) == True

    assert bst.preorder_traversal() == []
    assert bst.inorder_traversal() == []
    assert bst.postorder_traversal() == []


#         50
#        /   \
#       30    70
#      / \    / \
#     20  40 60  80

# After remove 30
#         50
#        /   \
#       40    70
#      /     / \
#     20    60  80

# After re-insert 30
#         50
#        /   \
#       40    70
#      /     / \
#    20    60  80
#      \
#      30

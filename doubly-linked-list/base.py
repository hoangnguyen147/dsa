class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
            new_node.prev_node = current_node

    def insert(self, data, position):
        new_node = Node(data)
        if position < 0: return False
        if position == 0:
            new_node.next_node = self.head
            new_node.prev_node = None
            if self.head:
                self.head.prev_node = new_node
            self.head = new_node
        else:
            current_node = self.head
            count = 0
            while current_node and count < position:
                current_node = current_node.next_node
                count += 1
            if not current_node:
                return False
            new_node.prev_node = current_node.prev_node
            new_node.next_node = current_node
            if current_node.prev_node:
                current_node.prev_node.next_node = new_node
            else:
                self.head = new_node
            current_node.prev_node = new_node
        return True

    def delete(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                if current_node.prev_node:
                    current_node.prev_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node.prev_node
                return True
            current_node = current_node.next_node
        return False

    def traverse(self):
        current_node = self.head
        if current_node is None:
            return "Empty List"
        printStr = str(current_node.data)
        current_node = current_node.next_node
        while current_node:
            printStr += " <-> " + str(current_node.data)
            current_node = current_node.next_node
        return printStr

    def search(self, key):
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == key:
                return position
            current_node = current_node.next_node
            position += 1
        return -1

    def sort(self):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            next_node = current_node.next_node
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next_node
            current_node = current_node.next_node

def test_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()

    assert doubly_linked_list.traverse() == "Empty List"
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)
    doubly_linked_list.append(4)
    doubly_linked_list.append(5)
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [1, 2, 3, 4, 5])
    assert doubly_linked_list.search(1) == 0
    assert doubly_linked_list.delete(3) == True
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [1, 2, 4, 5])
    assert doubly_linked_list.delete(7) == False
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [1, 2, 4, 5])
    assert doubly_linked_list.search(4) == 2
    doubly_linked_list.append(3)
    doubly_linked_list.append(8)
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [1, 2, 4, 5, 3, 8])
    doubly_linked_list.sort()
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [1, 2, 3, 4, 5, 8])

def test_doubly_linked_list_2():
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.append(8)
    doubly_linked_list.append(7)
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)
    doubly_linked_list.sort()
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [1, 2, 3, 7, 8])
    assert doubly_linked_list.search(8) == 4
    assert doubly_linked_list.insert(5, 2) == True
    assert doubly_linked_list.insert(9, 12) == False
    assert doubly_linked_list.insert(11, -1) == False
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [1, 2, 5, 3, 7, 8])
    assert doubly_linked_list.search(3) == 3
    assert doubly_linked_list.delete(7) == True
    assert doubly_linked_list.delete(1) == True
    assert doubly_linked_list.delete(3) == True
    assert doubly_linked_list.delete(8) == True
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [2, 5])
    assert doubly_linked_list.delete(3) == False
    assert doubly_linked_list.delete(2) == True
    assert doubly_linked_list.traverse() == " <-> ".join(str(i) for i in [5])
    assert doubly_linked_list.delete(5) == True
    assert doubly_linked_list.traverse() == "Empty List"

if __name__ == "__main__":
    test_doubly_linked_list()
    test_doubly_linked_list_2()

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position < 0: return False
        if position == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            count = 0
            while current_node and count < position - 1:
                current_node = current_node.next_node
                count += 1
            if not current_node:
                return False
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
        return True

    def delete(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next_node
            return True
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next_node
        if not current_node:
            return False
        prev.next_node = current_node.next_node
        return True

    def traverse(self):
        current_node = self.head
        if current_node is None:
            return "Empty List"
        printStr = str(current_node.data)
        current_node = current_node.next_node
        while current_node:
            printStr += " -> " + str(current_node.data)
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

def test_linked_list():
    linked_list = LinkedList()

    assert linked_list.traverse() == "Empty List"
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    assert linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 3, 4, 5])
    assert linked_list.search(1) == 0
    assert linked_list.delete(3) == True
    assert linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 4, 5])
    assert linked_list.delete(7) == False
    assert linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 4, 5])
    assert linked_list.search(4) == 2
    linked_list.append(3)
    linked_list.append(8)
    assert linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 4, 5, 3, 8])
    linked_list.sort()
    assert linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 3, 4, 5, 8])

def test_linked_list_2():
    linked_list = LinkedList()

    linked_list.append(8)
    linked_list.append(7)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.sort()
    assert linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 3, 7, 8])
    assert linked_list.search(8) == 4
    assert linked_list.insert(5, 2) == True
    assert linked_list.insert(9, 12) == False
    assert linked_list.insert(11, -1) == False
    assert linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 5, 3, 7, 8])
    assert linked_list.search(3) == 3
    assert linked_list.delete(7) == True
    assert linked_list.delete(1) == True
    assert linked_list.delete(3) == True
    assert linked_list.delete(8) == True
    assert linked_list.traverse() == " -> ".join(str(i) for i in [2, 5])
    assert linked_list.delete(3) == False
    assert linked_list.delete(2) == True
    assert linked_list.traverse() == " -> ".join(str(i) for i in [5])
    assert linked_list.delete(5) == True
    assert linked_list.traverse() == "Empty List"
    assert linked_list.delete(2) == False
    assert linked_list.traverse() == "Empty List"

if __name__ == "__main__":
    test_linked_list()
    test_linked_list_2()

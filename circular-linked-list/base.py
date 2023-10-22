class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next_node = self.head
        else:
            current_node = self.head
            while current_node.next_node != self.head:
                current_node = current_node.next_node
            current_node.next_node = new_node
            new_node.next_node = self.head

    def insert(self, data, position):
        new_node = Node(data)
        if position < 0: return False
        if position == 0:
            new_node.next_node = self.head
            current_node = self.head
            while current_node.next_node != self.head:
                current_node = current_node.next_node
            current_node.next_node = new_node
            self.head = new_node
        else:
            current_node = self.head
            count = 0
            while count < position - 1 and current_node.next_node != self.head:
                current_node = current_node.next_node
                count += 1
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
        return True

    def delete(self, key):
        if not self.head:
            return False
        
        if self.head.data == key and self.head.next_node == self.head:
            self.head = None
            return True
        
        current_node = self.head

        if self.head.data == key:
            while current_node.next_node != self.head:
                current_node = current_node.next_node
            current_node.next_node = self.head.next_node
            self.head = current_node.next_node
            return True
        
        while current_node.next_node != self.head and current_node.next_node.data != key:
            current_node = current_node.next_node
        
        if current_node.next_node.data == key:
            temp_node = current_node.next_node
            current_node.next_node = temp_node.next_node
            return True

        return False

    def traverse(self):
        if not self.head:
            return "Empty List"
        printStr = str(self.head.data)
        current_node = self.head.next_node
        if current_node == self.head:
            return printStr
        while True:
            printStr += " -> " + str(current_node.data)
            current_node = current_node.next_node
            if current_node == self.head:
                break
        return printStr

    def search(self, key):
        if not self.head:
            return -1
        current_node = self.head
        position = 0
        while True:
            if current_node.data == key:
                return position
            current_node = current_node.next_node
            position += 1
            if current_node == self.head:
                break
        return -1

    def sort(self):
        if not self.head:
            return
        current_node = self.head
        while True:
            next_node = current_node.next_node
            while next_node != self.head:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next_node
            current_node = current_node.next_node
            if current_node == self.head:
                break


def test_circular_linked_list():
    circular_linked_list = CircularLinkedList()

    assert circular_linked_list.traverse() == "Empty List"
    circular_linked_list.append(1)
    circular_linked_list.append(2)
    circular_linked_list.append(3)
    circular_linked_list.append(4)
    circular_linked_list.append(5)
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 3, 4, 5])
    assert circular_linked_list.search(1) == 0
    assert circular_linked_list.delete(3) == True
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 4, 5])
    assert circular_linked_list.delete(7) == False
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 4, 5])
    assert circular_linked_list.search(4) == 2
    circular_linked_list.append(3)
    circular_linked_list.append(8)
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 4, 5, 3, 8])
    circular_linked_list.sort()
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 3, 4, 5, 8])

def test_circular_linked_list_2():
    circular_linked_list = CircularLinkedList()

    circular_linked_list.append(8)
    circular_linked_list.append(7)
    circular_linked_list.append(1)
    circular_linked_list.append(2)
    circular_linked_list.append(3)
    circular_linked_list.sort()
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 3, 7, 8])
    assert circular_linked_list.search(8) == 4
    assert circular_linked_list.insert(5, 2) == True
    assert circular_linked_list.insert(9, 12) == True
    assert circular_linked_list.insert(11, -1) == False
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [1, 2, 5, 3, 7, 8, 9])
    assert circular_linked_list.search(3) == 3
    assert circular_linked_list.delete(7) == True
    assert circular_linked_list.delete(1) == True
    assert circular_linked_list.delete(3) == True
    assert circular_linked_list.delete(8) == True
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [2, 5, 9])
    assert circular_linked_list.delete(3) == False
    assert circular_linked_list.delete(2) == True
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [5, 9])
    assert circular_linked_list.delete(5) == True
    assert circular_linked_list.delete(9) == True
    assert circular_linked_list.traverse() == "Empty List"

def test_circular_linked_list_3():
    circular_linked_list = CircularLinkedList()

    circular_linked_list.append(1)
    circular_linked_list.append(2)
    circular_linked_list.append(3)
    circular_linked_list.append(4)
    circular_linked_list.append(5)
    assert circular_linked_list.delete(1) == True
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [2, 3, 4, 5])
    assert circular_linked_list.delete(2) == True
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [3, 4, 5])
    assert circular_linked_list.delete(3) == True
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [4, 5])
    assert circular_linked_list.delete(4) == True
    assert circular_linked_list.traverse() == " -> ".join(str(i) for i in [5])
    assert circular_linked_list.delete(5) == True
    assert circular_linked_list.traverse() == "Empty List"

if __name__ == "__main__":
    test_circular_linked_list()
    test_circular_linked_list_2()
    test_circular_linked_list_3()

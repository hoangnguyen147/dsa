class Node:
 
    def __init__(self, data):
        self.data = data
        self.next_node = None

class Queue:
 
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
    
    def getFront(self):
        return self.front
 
    def enQueue(self, item):
        temp = Node(item)
 
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next_node = temp
        self.rear = temp
 
    def deQueue(self):
 
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next_node
 
        if(self.front == None):
            self.rear = None

        return temp.data
    
    def toString(self):

        iter_node = self.front
        if self.isEmpty():
            return "Empty Queue"
 
        else:
            result_str = ""
            while(iter_node != None):
                result_str += str(iter_node.data)
                iter_node = iter_node.next_node
                if(iter_node != None):
                    result_str += " -> "
            return result_str
 
 
if __name__ == '__main__':
    q = Queue()
    q.enQueue(10)
    q.enQueue(20)
    q.deQueue()
    q.deQueue()
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    q.deQueue()
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))

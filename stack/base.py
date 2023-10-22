 
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
 
 
class Stack:
 
    def __init__(self):
        self.head = None
 
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
 
    def push(self, data):
 
        if self.head == None:
            self.head = Node(data)
 
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
 
    def pop(self):
 
        if self.isEmpty():
            return None
 
        else:
            popped_node = self.head
            self.head = self.head.next_node
            popped_node.next_node = None
            return popped_node.data
 
    def peek(self):
 
        if self.isEmpty():
            return None
 
        else:
            return self.head.data
 
    def toString(self):

        iter_node = self.head
        if self.isEmpty():
            return "Empty Stack"
 
        else:
            result_str = ""
            while(iter_node != None):
                result_str += str(iter_node.data)
                iter_node = iter_node.next_node
                if(iter_node != None):
                    result_str += " -> "
            return result_str
 
 
# Driver code
if __name__ == "__main__":
  MyStack = Stack()
   
  MyStack.push(11)
  MyStack.push(22)
  MyStack.push(33)
  MyStack.push(44)
 
  print(MyStack.toString())
 
  print("\nTop element is ", MyStack.peek())
 
  MyStack.pop()
  MyStack.pop()
 
  print(MyStack.toString())
 
  print("\nTop element is ", MyStack.peek())
 
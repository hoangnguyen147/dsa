import unittest
from base import Stack

class TestStack(unittest.TestCase):
    def test_case_1(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.toString(), "3 -> 2 -> 1")

    def test_case_2(self):
        stack = Stack()
        self.assertEqual(stack.toString(), "Empty Stack")

    def test_case_3(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_case_4(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.toString(), "Empty Stack")


if __name__ == '__main__':
    unittest.main()

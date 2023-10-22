import unittest
from base import Queue

class TestQueue(unittest.TestCase):
    def test_case_1(self):
        queue = Queue()
        queue.enQueue(1)
        queue.enQueue(2)
        queue.enQueue(3)
        queue.enQueue(4)

        self.assertEqual(queue.toString(), "1 -> 2 -> 3 -> 4")

        self.assertEqual(queue.deQueue(), 1)
        self.assertEqual(queue.deQueue(), 2)
        self.assertEqual(queue.deQueue(), 3)
        self.assertEqual(queue.deQueue(), 4)

        self.assertEqual(queue.toString(), "Empty Queue")

    def test_case_2(self):
        queue = Queue()
        self.assertEqual(queue.isEmpty(), True)
        queue.enQueue(1)
        self.assertEqual(queue.isEmpty(), False)

    def test_case_3(self):
        queue = Queue()
        self.assertEqual(queue.getFront(), None)
        queue.enQueue(1)
        self.assertEqual(queue.getFront().data, 1)
        queue.enQueue(2)
        self.assertEqual(queue.getFront().data, 1)

    def test_case_4(self):
        queue = Queue()
        queue.enQueue(1)
        queue.enQueue(2)

        self.assertEqual(queue.deQueue(), 1)

        queue.enQueue(3)
        queue.enQueue(4)

        self.assertEqual(queue.deQueue(), 2)

        queue.enQueue(5)

        self.assertEqual(queue.toString(), "3 -> 4 -> 5")


if __name__ == '__main__':
    unittest.main()

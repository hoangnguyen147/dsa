import unittest

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_min(arr):
    if not arr:
        return None
    return min(arr)

def find_max(arr):
    if not arr:
        return None
    return max(arr)

def append_element(arr, element):
    arr.append(element)

def insert_element(arr, element, position):
    arr.insert(position, element)

def delete_element(arr, target):
    if target in arr:
        arr.remove(target)

def traverse_array(arr):
    for element in arr:
        print(element, end=" ")

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [64, 25, 12, 22, 11]

delete_element(arr, 12)

traverse_array(arr)

class TestArrayFunctions(unittest.TestCase):
    def test_linear_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 3), 2)
        self.assertEqual(linear_search(arr, 6), -1)

    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)
        self.assertEqual(binary_search(arr, 6), -1)

    def test_find_min(self):
        arr = [5, 3, 7, 1, 2]
        self.assertEqual(find_min(arr), 1)
        self.assertEqual(find_min([]), None)

    def test_find_max(self):
        arr = [5, 3, 7, 1, 2]
        self.assertEqual(find_max(arr), 7)
        self.assertEqual(find_max([]), None)

    def test_append_element(self):
        arr = [1, 2, 3]
        append_element(arr, 4)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_insert_element(self):
        arr = [1, 2, 4]
        insert_element(arr, 3, 2)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_delete_element(self):
        arr = [1, 2, 3, 4]
        delete_element(arr, 3)
        self.assertEqual(arr, [1, 2, 4])

    def test_selection_sort(self):
        arr = [4, 2, 1, 3, 5]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_insertion_sort(self):
        arr = [4, 2, 1, 3, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

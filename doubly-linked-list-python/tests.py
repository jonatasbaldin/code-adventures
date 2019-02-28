import unittest

from doubly_linked_list import Node, DoublyLinked


class LinkedListTest(unittest.TestCase):
    def test_append(self):
        ll = DoublyLinked()
        ll.append(1)
        ll.append(2)

        self.assertEqual(ll.first_node.data, 1)
        self.assertEqual(ll.head.data, 2)

    def test_traverse(self):
        ll = DoublyLinked()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        all_nodes = ll.traverse()

        self.assertEqual(all_nodes, [1, 2, 3])

    def test_delete(self):
        ll = DoublyLinked()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(6)

        ll.delete(5)

        all_nodes = ll.traverse()

        self.assertEqual(all_nodes, [1, 2, 3, 4, 6])

    def test_delete_last_element(self):
        ll = DoublyLinked()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(6)

        ll.delete(6)

        all_nodes = ll.traverse()

        self.assertEqual(all_nodes, [1, 2, 3, 4, 5])
        self.assertEqual(ll.head.data, 5)

    def test_delete_first_element(self):
        ll = DoublyLinked()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(6)

        ll.delete(1)

        all_nodes = ll.traverse()

        self.assertEqual(all_nodes, [2, 3, 4, 5, 6])
        self.assertEqual(ll.first_node.data, 2)


if __name__ == '__main__':
    unittest.main()
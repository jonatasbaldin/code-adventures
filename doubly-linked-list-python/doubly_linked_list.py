"""
A Doubly Linked List!
https://www.geeksforgeeks.org/doubly-linked-list/

Properties:
- Composed of n nodes
- Each node knows its next and previous node
- "Dynamic Arrays"

Possible operations:
- Append, O(1) – not necessary to traverse the whole list to append, since we know the last element
- Traverse, O(n) – goes through every element
- Delete, O(n) – goes through every element if necessary
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

    def __repr__(self):
        return f"<Node '{self.data}'>"


class DoublyLinked:
    def __init__(self):
        self.first_node = None
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if self.first_node is None:
            self.first_node = new_node

        if self.head is not None:
            self.head.next_node = new_node

        new_node.previous_node = self.head

        self.head = new_node

    def delete(self, data):
        """
        - Get the node that contain this data
        - Points its next_node to its previous_node.next_node
        - Verify if is last_element
        - Verify if is first_element
        """
        
        node = self.first_node
        node_to_be_deleted = None

        while node.next_node:
            if node.data == data:
                node_to_be_deleted = node
                break
            node = node.next_node

        # Check the last node that will fail the above condition
        if node.data == data:
            node_to_be_deleted = node

        if node_to_be_deleted:
            previous_node = node_to_be_deleted.previous_node
            next_node = node_to_be_deleted.next_node

            # Change head if deleting the last element
            if not next_node:
                self.head = previous_node

            # Change first_node if deleteing the first element
            if not previous_node:
                self.first_node = next_node
                return

            previous_node.next_node = next_node

        return        

    def traverse(self, node=None):
        all_nodes = []

        if not node:
            node = self.first_node
        
        while node.next_node:
           all_nodes.append(node.data)
           node = node.next_node

        # Appends the last node that will fail the above condition
        all_nodes.append(node.data)

        return all_nodes

    def __repr__(self):
        return f"<DoublyLinked '{self.head}'>"
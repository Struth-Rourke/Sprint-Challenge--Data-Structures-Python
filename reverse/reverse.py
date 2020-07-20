class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    ## CODE HERE:
    def reverse_list(self, node, prev):
        # if node does not exist
        if node is None:
            return
        # if next does not exist
        if node.next_node is None:
            # node.next_node equals previous node (reversing)
            node.next_node = prev
            # head = node (reset to head)
            self.head = node
            return
        else:
            # recursive to reverse next_node and node to prev
            self.reverse_list(node.next_node, node)
        # setting next to prev as a reversal
        node.next_node = prev

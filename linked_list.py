from node import Node


class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)
        self.previous_node = None
        self.next_node = None

    def get_head_node(self):
        return self.head_node

    def insert_value_front(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node

    def stringfy_list(self, separator=None):
        value_list = []
        current_node = self.get_head_node()
        while current_node:
            value_list.append(current_node.get_value())
            current_node = current_node.get_next_node()
        if separator:
            return separator.join(value_list)
        return value_list

    def remove_node(self, value):
        current_node = self.get_head_node()
        if current_node.get_value() == value:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value:
                    current_node.set_next_node(next_node.get_next_node)
                    current_node = None
                else:
                    current_node = next_node

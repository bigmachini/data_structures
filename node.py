class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def get_previous_node(self):
        return self.previous_node

    def set_next_node(self, node):
        self.next_node = node

    def set_previos_node(self, node):
        self.previous_node = node

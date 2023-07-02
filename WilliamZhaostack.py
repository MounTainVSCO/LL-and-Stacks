from WilliamZhaonode import LinkedList

class Stack:
    def __init__(self):
        self.data = None
        self.length = 0

    def create_stack(self):
        self.data = LinkedList()

    def push(self, data):
        self.data.append_node(data)
        self.length += 1

    def peek(self):
        if self.is_empty():
            return None
        return self.data.get_last_node()
    
    def is_empty(self):
        return self.data.get_len() == 0
    
    def pop(self):
        if self.is_empty():
            return None
        self.data.delete_end_node()
        self.length -= 1

    def delete_stack(self):
        self.data.deleteAllNodes()
        self.length = 0



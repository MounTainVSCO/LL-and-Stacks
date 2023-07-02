class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_node(self, data):
        data_node = Node(data)
        
        if self.head is None:
            self.head = data_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = data_node

    def delete_end_node(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None

        
    def get_last_node(self):
        curr = self.head
        if self.head is None:
            return None
        while curr.next is not None:
            curr = curr.next
        return curr

    
    def get_len(self):
        len = 0
        curr = self.head
        while curr is not None: 
            len += 1
            curr = curr.next
        return len
    
    def deleteAllNodes(self):
        
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None



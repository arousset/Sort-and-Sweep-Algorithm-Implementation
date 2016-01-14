class Node:
    def __init__ (self, d, nn = None):
        self.data = d
        self.next_node = nn
        
    def get_next (self):
        return self.next_node
    
    def set_next (self, nn):
        self.next_node = nn
        
    def get_data (self):
        return self.data
    
    def set_data (self, d):
        self.data = d

class LinkedList:
    def __init__ (self, r = None):
        self.root = r
        self.size = 0
        
    def get_size (self):
        return self.size
    
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
        
    def remove (self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

'''myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)
print(myList.remove(12))'''
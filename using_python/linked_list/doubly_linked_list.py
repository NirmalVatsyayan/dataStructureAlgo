class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
 
class DoublyList(object):
 
    head = None
    tail = None
 
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
 
    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
 
            current_node = current_node.next
    
    def search( self, search_data ) :
        current = self.head
        if current != None :
            while current != None :
                print(">>>>  ", current.data, " >>> ",search_data)
                if (current.data == search_data):
                    return current

                if current.next == None:
                    break
                current = current.next
                
            if (current.data == search_data):
                return current
        return None

    def show(self):
        print("Showing list data:")
        current_node = self.head
        while current_node is not None:
            if hasattr(current_node, "data"):
                print(current_node.data)

            current_node = current_node.next
        print("*"*50)
 
 
d = DoublyList()
 
d.append(5)
d.append(6)
d.append(50)
d.append(30)
 
d.show()
 
d.remove(50)
d.remove(5)
 
d.show()
print(d.search(30))

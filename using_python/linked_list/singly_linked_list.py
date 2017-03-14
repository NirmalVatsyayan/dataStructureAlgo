import os

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data
        return self.data

    def getData(self):
    	return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

class SinglyLinkList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.listLength() == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)

        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(newNode)

    def listLength(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        return count

    def print_list(self):
        current = self.head
        print("List Start.")
        while current != None:
            print(current.getData())
            current = current.getNext()

        print("List End.")


    def search_list(self, data):
        current = self.head
        found = False
        
        while current != None:
            if current.getData() == data:
                found = True
                break

            current = current.getNext()

        if found is not True:
            return None
        
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':
    l_list = SinglyLinkList()

    l_list.insertAtBeginning(100)
    for i in range(101, 110):
    	l_list.insertAtEnd(i)
    
    l_list.print_list()

    print(l_list.listLength())
    print(os.getcwd())

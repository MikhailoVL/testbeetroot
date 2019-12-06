class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def found_linked_list(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def chenge_element(self, item):
        current = self.head
        previos = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previos = current
                current = current.getNext()
        if previos is None:
            self.head = current.getNext()
        else:
            previos.setNext(current.getNext())

list_1 = LinkedList()
list_1.add(1)
list_1.add(2)

print(list_1.found_linked_list(1))

class Node_too:
    def __init__(self, next = None, prev = None, data= None):
        self.data = initdata
        self.prev = prev
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
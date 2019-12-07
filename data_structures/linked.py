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
        a = self.size()
        if self.size():
            current = self.head
            print(str(current.getData()) + "nfnf")
            while a > 0:
                if current.getData() <= temp.getData():
                    temp.setNext(current.getNext())
                    # current.setNext(temp)
                    current = current.getNext()
                    # print(current.getData())

                else:
                    temp.setNext(current.getNext())
                    current.setNext(temp)
                    current = current.getNext()
                    current = current.getNext()
                a -=1
        else:
            temp.setNext(self.head)
            self.head = temp

    def show(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()


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
list_1.add(14)
list_1.add(2)
list_1.add(1)
list_1.show()
list_1.add(12)
print("_____")

list_1.add(2)

print("______________")
a = list_1.size()
print(a)

print(list_1.found_linked_list(1))


class Node_too:
    def __init__(self, initdata, next=None, prev=None, data=None, ):
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

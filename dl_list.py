class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def getNext(self):
        return self.next

    def setPrev(self,newprev):
        self.prev = newprev

    def getPrev(self):
        return self.prev


class DL_List:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def insert(self, item):
        """
        Insert new node at the beginning
        :param item:
        :return:
        """
        temp = Node(item)

        if self.head == None:
            temp.setNext(temp)
            temp.setPrev(temp)
            self.head = temp
        else:
            temp.setPrev(self.head.getPrev())
            temp.getPrev().setNext(temp)
            temp.setNext(self.head)
            self.head.setPrev(temp)

        self.count += 1

    def size(self):
        return self.count

    def search(self, item):
        found = False
        temp = self.head
        counter = 0
        size = self.size()

        while not found and counter < size:
            if temp.getData() == item:
                found = True
            else:
                counter += 1
                temp = temp.getNext()

        return found


    def __str__(self):
        temp = self.head
        out = []

        for i in range(self.size()):
            out.append(temp.getData())
            temp = temp.getNext()

        return str(out)

"""
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
"""

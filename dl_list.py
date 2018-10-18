class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, newdata):
        self.__data = newdata

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, newnext):
        self.__next = newnext

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self,newprev):
        self.__prev = newprev


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
            temp.next = temp
            temp.prev = temp
            self.head = temp
        else:
            temp.prev = self.head.prev
            temp.prev.next = temp
            temp.next = self.head
            self.head.prev = temp

        self.count += 1

    def size(self):
        return self.count

    def search(self, item):
        found = False
        temp = self.head
        counter = 0
        size = self.size()

        while not found and counter < size:
            if temp.data == item:
                found = True
            else:
                counter += 1
                temp = temp.next

        return found


    def __str__(self):
        temp = self.head
        out = []

        for i in range(self.size()):
            out.append(temp.data)
            temp = temp.next

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

if __name__ == "__main__":
    x = DL_List()
    x.insert(10)
    x.insert(20)
    x.insert(-3)
    x.insert(99)
    print(x)
    print(x.search(20))
    print(x.search(99))
    print(x.search(10))
    print(x.search(44))
class SLinkedListNode:
    
    def __init__(self, initData, initNext):
        # constructs a new node and initializes it to contain 
        # the given object (initData) and links to the given next 
        # and previous nodes. 
        self.data = initData
        self.next = initNext


    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next= newNext


class SLinked_List:
    
    # creates a new doubly linked list
    # head and tail are initialized to None
    def __init__(self):
        self.head=None
        self.__size=0

    def getHead(self):
        return self.head
   
    # adds a new node with data = item to the end of the list    
    def append(self, item):
        temp = SLinkedListNode(item, None)
        if (self.head == None):
            self.head=temp
        else:
            current = self.head;
            while (current.getNext() != None):
                current = current.getNext()
            current.setNext(temp)
        self.__size +=1

    def __str__(self):
        output = []
        current = self.head
        while current:
            output.append(current.data)
            current = current.next
        output=[str(i) for i in output]
        return "->".join(output)

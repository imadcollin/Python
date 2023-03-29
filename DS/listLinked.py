class Node:
    def __init__(self,dataval) -> None:
        self.dataval = dataval
        self.nextval = None 

class SlinkedList: 
    def __init__(self) -> None:
        self.headval =None
        
    def printList(self):
        curNode=self.headval 
        while curNode is not None: 
            print(curNode.dataval)
            curNode= curNode.nextval
            
    def insertFront(self, newData):
        newNode = Node(newData)
        newNode.nextval= self.headval
        self.headval=newNode
    
    def insertEnd(self, newData):
        newNode = Node(newData)
        curNode = self.headval
        while curNode is not None:
            curNode = curNode.nextval
        curNode.nextval= newNode
def createLinkedList():
    list1= SlinkedList()
    list1.headval = Node(1) 
    e2= Node(2)
    e3= Node(3)

    list1.headval.nextval =e2 
    e2.nextval =e3  
    return list1

## Print List 
createLinkedList().printList()

# Insert Front
oldList = createLinkedList()
newList = oldList.insertFront(0)
newList.printList()

# Insert End 
#oldList2 = createLinkedList()
#newList2 = oldList2.insertFront(4)
#newList2.printList()


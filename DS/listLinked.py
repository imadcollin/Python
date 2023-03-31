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
        if self.headval is None: 
            self.headval= newNode
            return
    
        while (curNode.nextval):
            curNode = curNode.nextval
        curNode.nextval= newNode
        
    def nextToNode(self, node, newData):
        if node is None:
            print('Node not exist')
            return
        else:
            newNode= Node(newData)
            node.nextval = newNode
            newNode.nextval=node.nextval.nextval
            #newNode.dataval = node.dataval
            
            
def createLinkedList():
    list1= SlinkedList()
    list1.headval = Node(1) 
    e2= Node(2)
    e3= Node(3)

    list1.headval.nextval =e2 
    e2.nextval =e3  
    return list1

## Print List 
print('####### Print list ######')
createLinkedList().printList()

# Insert Front
print('####### Insert Front ######')
oldList = createLinkedList()
oldList.insertFront(0)
oldList.printList()

# Insert End 
print('####### Insert End #####')
oldList2 = createLinkedList()
oldList2.insertEnd(4)
oldList2.printList()

# Insert Next To 
print('####### Insert Next To #####')
oldList3 = createLinkedList()
oldList3.nextToNode(oldList3.headval.nextval,11)
oldList3.printList()
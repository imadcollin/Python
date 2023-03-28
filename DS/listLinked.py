class Node:
    def __init__(self,dataval) -> None:
        self.dataval = dataval
        self.nextval = None 

class SlinkedList: 
    def __init__(self) -> None:
        self.headval =None

list1= SlinkedList()
list1.headval = Node("Mon") 
e2= Node("Tue")
e3= Node("Wed")

list1.headval.nextval =e2 
e2.nextval =e3      


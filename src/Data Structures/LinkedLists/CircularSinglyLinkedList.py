class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
class CircularSinglyLinkedList:
    def __init__(self, values = None):
        self.head = Node()
        
    def __iter__(self):
        tmpNode =  self.head.next
        if (tmpNode==None):
            return tmpNode
        else:
            while tmpNode:
                yield tmpNode
                tmpNode = tmpNode.next
                if (tmpNode==self.head.next):
                    return None
    
    def __str__(self):
        values = ['|'+str(x.value)+', '+str(x.next)+'|' for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        tmpNode = self.head.next
        if (tmpNode==None):
            return 0
        else:
            while tmpNode:
                result += 1
                tmpNode = tmpNode.next
                if (tmpNode==self.head.next):
                    break                
        return result
    
    # add a node in any valid index
    def addNode(self, value, index):
        newNode = Node(value)
        assert int(index) == index, 'The index must be an integer'
        if (index > len(self) or index < 0):
            print("Index out of bounds")
            return None
        elif (index == 0):
            tmpNode = self.head.next
            if (tmpNode == None):
                self.head.next = newNode
                newNode.next = newNode
            else:
                self.getLastNode().next = newNode
                newNode.next = tmpNode
                self.head.next = newNode
        else:
            tmpNode = self.head.next
            count = 1
            while tmpNode:
                if (index == count):
                    newNode.next = tmpNode.next
                    tmpNode.next = newNode
                    break
                tmpNode = tmpNode.next
                if (tmpNode == self.head.next):
                    break                 
                count += 1
        return self
    
    # return last node
    def getLastNode(self):
        return self.findNodeAtIndex(len(self)-1)
    
    # find all occurences of the search key
    def findIndicesOfNode(self, searchKey):
        indices = []
        tmpNode = self.head.next
        if (tmpNode == None):
            return indices
        count = 0
        while tmpNode:
            if (tmpNode.value == searchKey):
                indices.append(count)
            tmpNode = tmpNode.next
            count += 1
            if (tmpNode == self.head.next):
                break               
        return indices
    
    # find the node at a valid index
    def findNodeAtIndex(self, index):
        assert int(index) == index, 'The index must be an integer'
        if (index >= len(self) or index < 0):
            print("Index out of bounds")
            return None
        tmpNode = self.head.next
        if (tmpNode==None):
            return None
        count = 0
        while tmpNode:
            if (index == count):
                return tmpNode
            tmpNode = tmpNode.next
            count += 1
            if (tmpNode == self.head.next):
                break   
        return None
    
    # delete a node from any valid index
    def removeNode(self, index):
        tmpNode = Node()
        assert int(index) == index, 'The index must be an integer'
        if (index >= len(self) or index < 0):
            print("Index out of bounds")
            return None
        elif (index == 0):
            if(len(self) == 1):
                self.head.next = None
            else:
                self.getLastNode().next = self.head.next.next
                self.head.next = self.head.next.next
        else:
            if (index == len(self)-1):
                lastNodeFlag = True
            else:
                lastNodeFlag = False
            tmpNode = self.head.next
            count = 1
            while tmpNode:
                if (index == count):
                    if (not(lastNodeFlag)):
                        tmpNode.next = tmpNode.next.next
                    else:
                        tmpNode.next = self.head.next
                    break
                tmpNode = tmpNode.next
                count += 1
                if (tmpNode == self.head.next):
                    break                   
        return self        
           
    # update an existing node's value
    def updateNode(self, value, index):
        tmpNode = Node()
        assert int(index) == index, 'The index must be an integer'
        if (index >= len(self) or index < 0):
            print("Index out of bounds")
            return None
        elif (index == 0):
            tmpNode = self.head.next
            tmpNode.value = value
        else:
            tmpNode = self.head.next
            count = 1
            while tmpNode:
                if (index == count):
                    tmpNode.value = value
                    break
                tmpNode = tmpNode.next
                count += 1
                if (tmpNode == self.head.next):
                    break                  
        return self        


# customCLL = CircularSinglyLinkedList()
# customCLL.addNode(100, 0)
# customCLL.addNode(130, 1)
# customCLL.addNode(490, 0)
# customCLL.addNode(190, 3)
# customCLL.addNode(300, 3)
# customCLL.addNode(100, 1)
# customCLL.addNode(290, 2)
# customCLL.addNode(200, 1)
# print(customCLL)
# print(len(customCLL))
# print(customCLL.findIndicesOfNode(100))
# print(customCLL.findNodeAtIndex(0))
# customCLL.updateNode(888, 0)    
# print(customCLL)
# customCLL.removeNode(7)  
# customCLL.removeNode(0)  
# customCLL.removeNode(0)  
# print(customCLL)
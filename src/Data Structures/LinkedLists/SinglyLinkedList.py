class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
class SinglyLinkedList:
    def __init__(self, values = None):
        self.head = None
        
    def __iter__(self):
        tmp =  self.head
        while tmp:
            yield tmp
            tmp = tmp.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    # add a node in any valid index
    def addNode(self, value, index):
        newNode = Node(value)
        tmpNode = Node()
        assert int(index) == index, 'The index must be an integer'
        if (index > len(self) or index < 0):
            print("Index out of bounds")
            return None
        elif (index == 0):
            tmpNode = self.head
            self.head = newNode
            newNode.next = tmpNode
        else:
            tmpNode = self.head
            count = 1
            while tmpNode:
                if (index == count):
                    newNode.next = tmpNode.next
                    tmpNode.next = newNode
                    break
                tmpNode = tmpNode.next
                count += 1
        return self
    
    # find all occurences of the search key
    def findIndicesOfNode(self, searchKey):
        tmpNode = self.head
        count = 0
        indices = []
        while tmpNode:
            if (tmpNode.value == searchKey):
                indices.append(count)
            tmpNode = tmpNode.next
            count += 1
        return indices
    
    # find the node at a valid index
    def findNodeAtIndex(self, index):
        assert int(index) == index, 'The index must be an integer'
        if (index > len(self) or index < 0):
            print("Index out of bounds")
            return None
        tmpNode = self.head
        count = 0
        while tmpNode:
            if (index == count):
                return tmpNode
            tmpNode = tmpNode.next
            count += 1
        return None
    
    # delete a node from any valid index
    def removeNode(self, index):
        tmpNode = Node()
        assert int(index) == index, 'The index must be an integer'
        if (index >= len(self) or index < 0):
            print("Index out of bounds")
            return None
        elif (index == 0):
            tmpNode = self.head
            self.head = tmpNode.next
        else:
            if (index == len(self)-1):
                lastNodeFlag = True
            else:
                lastNodeFlag = False
            tmpNode = self.head
            count = 1
            while tmpNode:
                if (index == count):
                    if (not(lastNodeFlag)):
                        tmpNode.next = tmpNode.next.next
                    else:
                        tmpNode.next = None
                    break
                tmpNode = tmpNode.next
                count += 1
        return self        
           
    # update an existing node's value
    def updateNode(self, value, index):
        tmpNode = Node()
        assert int(index) == index, 'The index must be an integer'
        if (index >= len(self) or index < 0):
            print("Index out of bounds")
            return None
        elif (index == 0):
            tmpNode = self.head
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
        return self        


# customLL = SinglyLinkedList()
# customLL.addNode(10, 0)
# customLL.addNode(100, 1)
# customLL.addNode(190, 2)
# customLL.addNode(300, 3)
# customLL.addNode(100, 4)
# customLL.addNode(490, 0)
# customLL.addNode(290, 2)
# customLL.addNode(200, 1)
# print(len(customLL))
# print(customLL.findIndicesOfNode(100))
# print(customLL.findNodeAtIndex(6))
# customLL.updateNode(888, 0)    
# customLL.removeNode(7)  
# customLL.removeNode(0)  
# print(customLL)
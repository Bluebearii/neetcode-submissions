class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val


#creates a new node, if there is no head node, current head and tail is now the new node
    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node    
            self.tail = new_node
        else:                   #confusing part. If the check is cleared, then we want to insert the head but we must relocate the previous head to the next
           new_node.next = self.head
           self.head = new_node
        self.size +=1




    def insertTail(self, val: int) -> None: 
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:                   #confusing part. If the check is cleared, then we want to insert the new node at self.tail.next because this points to None which is at the end of the list, then we rename the tail to the new_node because it has become the new last node
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

# Relearn this tomorrow bro youre kinda cooked
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        elif index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next

            if temp.next == None:
                self.tail = temp

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr != None:
            res.append(curr.val)
            curr= curr.next
        return res

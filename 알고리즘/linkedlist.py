class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class NodeMgmt:
    def __init__(self,data):
        self.head=Node(data)

    def add(self,data):
        if self.head=='':
            self.head=Node(data)
        else:
            node= self.head
            while node.next:
                node= node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self,data):
        if self.head =='':
            print("해당 값을 가진 노드가 없습니다")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next= node.next.next
                    del temp
                    return
                else:
                    node = node.next




class Node1:
    def __init__(self,data, next= None, prev = None):
        self.data= data
        self.next=next
        self.prev = prev

class NodeMgmt1:
    def __init__(self,data):
        self.head = Node1(data)
        self.tail = self.head


    def insert(self,data):
        if self.head == None:
            self.head = Node1(data)
            self.tail = self.head

        else:
            node1 = self.head
            while node1.next:
                node1 = node1.next
            new = Node1(data)
            node1.next = new
            new.prev = node1
            self.tail = new


    def desc1(self):
        node1 = self.head
        while node1.next:
            print(node1.data)
            node1 = node1.next

    def search_from_head(self,data):
        if self.head == None:
            return False

        node1 = self.head

        while node1:
            if node1.data == data:
                return node1
            else:
                node1 = node1.next
            return False
    def search_from_tail(self,data):
        if self.tail == None:
            return False

        node1 = self.tail

        while node1:
            if node1.data == data:
                return node1
            else:
                node1 = node1.prev
            return False


double_linked_list = NodeMgmt1(0)
for data in range(1,10):
    double_linked_list.insert(data)
double_linked_list.desc1()

node_3 = double_linked_list.search_from_head(1)

print(node_3)

node_3 = double_linked_list.search_from_tail(5)

print(node_3)
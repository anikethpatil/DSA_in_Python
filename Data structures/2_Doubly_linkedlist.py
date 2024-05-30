class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is None:
            return "Empty Linkedlist"
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '<-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        if self.head:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None, itr)
        itr.next = node

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if self.head is None:
            return "Empty Linkedlist"

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            itr = itr.next
            count += 1

    def revll(self):
        curr = self.head
        prev = None
        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev
        if prev:
            self.head = prev.prev

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(13)
    ll.insert_at_beginning(14)
    ll.insert_at_end(15)
    ll.insert_at(69,3)
    ll.printll()
    ll.remove_at(2)
    print("Before reversal")
    ll.printll()
    ll.revll()
    print("After reversal")
    ll.printll()
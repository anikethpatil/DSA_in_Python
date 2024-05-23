class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def printll(self):
        if self.head is None:
            return "Empty Linkedlist"
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)
    
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(data)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    
    def insert_at(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def remove_at(self,index):
        if self.head is None and index==0:
            return "Empty Linkedlist"
        itr=self.head
        count=0
        while itr.next:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1

    def revll(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev

if __name__=='__main__':
    ll=Linkedlist()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(13)
    ll.insert_at_beginning(14)
    ll.insert_at_end(15)
    ll.insert_at(69,2)
    ll.remove_at(2)
    print("Before Reversal")
    ll.printll()
    ll.revll()
    print("After Reversal")
    ll.printll()

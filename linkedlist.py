class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node()
    def ins_at_beg(self,val):
        temp=Node(val)
        if self.head.val == None:
            self.head=temp
            return
        temp.next=self.head
        self.head=temp
    def ins_at_end(self,val):
        temp=Node(val)
        if self.head.val is None:
            self.head = temp
            return
        t=self.head
        while t.next!=None:
            t=t.next
        t.next=temp
    def ins_at_pos(self,val,pos):
        if pos==1:
            self.ins_at_beg(val)
            return
        t=self.head
        c=2
        while c<pos and t.next!=None:
            t=t.next
            c+=1
        if c!=pos and t.next==None:
            print("Position not found.Insufficient nodes")
            return
        if c==pos and t.next==None:
            self.ins_at_end(val)
            return
        temp=Node(val)
        temp.next=t.next
        t.next=temp
    def ins_bw_nodes(self,val,prev,nxt):
        if val==None:
            print("Value should not be empty")
            return
        if prev==None or nxt==None:
            print("Prev and Next cannot be empty")
            return
        temp=Node(val)
        t=self.head
        while t.val!=prev and t.next.val!=nxt and t.next:
            t=t.next
        if t.next==None:
            print("Required position is not found.")
            return
        temp.next=t.next
        t.next=temp
    def del_a_node(self,val):
        t=self.head
        if t.val==val:
            self.head=self.head.next
            return
        while t.next.val!=val and t.next.next!=None:
            t=t.next
        if t.next.next==None and t.next.val==val:
            t.next=None
            return
        if t.next.next==None and t.next.val!=val:
            print("Not found")
            return
        t.next = t.next.next
    def del_at_beginning(self):
        t=self.head
        if t.val==None:
            print("Empty list")
            return
        self.head = self.head.next
    def del_at_end(self):
        t=self.head
        if t.val==None:
            print("Empty list")
            return
        while t.next.next!=None:
            t=t.next
        t.next=None
    def del_at_pos(self,pos):
        t=self.head
        if t.val==None:
            print("Empty List")
            return
        if pos==1:
            self.del_at_beginning()
            return
        c=1
        while c<pos-1 and t.next!=None:
            t=t.next
            c+=1
        if (t.next==None or t.next.val==None)  and c!=pos-1:
            print("Not found")
            return
        t.next = t.next.next
    def printList(self):
        t=self.head
        print("The list is:",end=" ")
        while t:
            print(t.val,end=" ")
            t=t.next
        print()
    def count(self):
        t=self.head
        if t.val==None:
            return 0
        c=0
        while t:
            t=t.next
            c+=1
        return c
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev

l=LinkedList()
print("Welcome to LinkedList operations!")
print("Select an option from the following:")
while(1):
    print("1.Insert a node  2.Insert at beginning  3.Insert at end  4.Insert at a position  5.Insert between two nodes")
    print("6.Delete a node  7.Delete at beginning  8.Delete at end  9.Delete at a position")
    print("10.Print linked list  11.Count  12.Reverse  13.Exit")
    print("Enter your option:",end=" ")
    n=int(input())
    if n==1:
        print("Enter the value to be inserted:")
        v=int(input())
        l.ins_at_end(v)
    elif n==2:
        print("Enter the value to be inserted at beginning:")
        v=int(input())
        l.ins_at_beg(v)
    elif n==3:
        print("Enter the value to be inserted at end:")
        v=int(input())
        l.ins_at_end(v)
    elif n==4:
        print("Enter the value to insert and position:")
        try:
            v,pos=map(int,input().split())
            l.ins_at_pos(v,pos)
        except:
            print("Enter both value of node and position values")
    elif n==5:
        print("Enter the value to be inserted: ")
        v=int(input())
        print("Enter the previous and next node values:")
        try:
            prev,nxt=map(int,input().split())
            l.ins_bw_nodes(v,prev,nxt)
        except:
            print("Enter both previous and next node values")
    elif n==6:
        print("Enter the value to delete:")
        v=int(input())
        l.del_a_node(v)
    elif n==7:
        l.del_at_beginning()
    elif n==8:
        l.del_at_end()
    elif n==9:
        print("Enter the deleting node position:")
        v=int(input())
        l.del_at_pos(v)
    elif n==10:
        l.printList()
    elif n==11:
        print(f"Number of nodes in linked list is: {l.count()}")
    elif n==12:
        l.reverse()
    elif n==13:
        print("Exiting")
        break
    else:
        print("Error!")
    if n!=10:
        l.printList()
    print("-"*15)

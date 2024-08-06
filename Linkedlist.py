class node:
    def __init__(self,data):
        self.data=data
        self.next= None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=node(data)
        if not self.head:
            self.head=newnode
            return
        lastnode=self.head
        while lastnode.next:
            lastnode=lastnode.next
        lastnode.next=newnode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print()
    def addafter(self,data,pos):
        newnode=node(data)
        currentnode=self.head
        currentpos=0
        while currentnode and currentpos < pos:
            currentnode=currentnode.next
            currentpos+=1
        if not currentnode:
            print("value out of bound")
            return
        newnode.next=currentnode.next
        currentnode.next=newnode
    def addbefore(self,data,pos):
        newnode=node(data)
        if pos==0:
            newnode.next=self.head
            self.head=newnode
            return
        
        currentnode=self.head
        currentpos=0
        while currentnode and currentpos<pos-1:
            currentnode=currentnode.next
            currentpos+=1
        newnode.next=currentnode.next
        currentnode.next=newnode

    def reverselist(self):
        prevnode=None
        currentnode=self.head
        while currentnode:
            nextnode=currentnode.next
            currentnode.next=prevnode
            prevnode=currentnode
            currentnode=nextnode
        self.head=prevnode
    def lenll(self):
        currentnode=self.head
        count=0
        while currentnode:
            currentnode=currentnode.next
            count=count+1
        return count
    def middle(self):
        currentnode=self.head
        a=self.lenll()
        b=a//2
        for _ in range(b):
            currentnode=currentnode.next
        print(currentnode.data)
    
   
            
       
l1=linkedlist()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)
l1.append(8)
l1.display()
l1.middle()



        


        


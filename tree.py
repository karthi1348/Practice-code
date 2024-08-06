
class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()
        

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def preordertraverse(self,root):
        result=[]
        if root:
            result.append(root.data)
            result=result+self.preordertraverse(root.left)
            result=result+self.preordertraverse(root.right)
        return result

    
root = node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.preordertraverse(root))

        


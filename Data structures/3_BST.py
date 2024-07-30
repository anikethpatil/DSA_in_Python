class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return 
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BSTNode(data)

    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def search(self,val):
        if val==self.data:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def max_ele(self):
        if self.right is None:
            return self.data
        return self.right.max_ele()
    
    def min_ele(self):
        if self.left is None:
            return self.data
        return self.left.min_ele()
    
    def sum_tree(self):
        treesum=self.data
        if self.left:
            treesum+=self.left.sum_tree()
        if self.right:
            treesum+=self.right.sum_tree()
        return treesum
    
    def deleteNode(self,val):
        #search value
        if val<self.data:
            self.left=self.left.deleteNode(val)
        elif val>self.data:
            self.right=self.right.deleteNode(val)
        else:
            #child
            if self.left is None and self.right is None:
                return None
            #1child parent
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            #2children parent
            min_val=self.right.min_ele()
            self.data=min_val
            self.right=self.right.deleteNode(min_val)
        return self
            
    
def build_tree(elements):
    root=BSTNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
    
if __name__=='__main__':
    numbers=[4,5,2,3,7,1,9,0]
    numbers_tree=build_tree(numbers)
    print("preorder:",numbers_tree.pre_order_traversal())
    print("inorder:",numbers_tree.in_order_traversal())
    print("postorder:",numbers_tree.post_order_traversal())
    
    print("Maximum element:",numbers_tree.max_ele())
    print("Minimum element:",numbers_tree.min_ele())
    print("Sum =",numbers_tree.sum_tree())
    print("Found:",numbers_tree.search(12))

    numbers_tree.deleteNode(2)
    print("After deletion",numbers_tree.in_order_traversal())

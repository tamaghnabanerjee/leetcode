'''
110. Balanced Binary Tree (Easy)
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self,value):
        self.root=Node(value)
    
    def insert(self,value):
        node=Node(value)
        if self.root==None:
           self.root=node
           return self.root
        curr=self.root
        while True:
            if curr.data==node.data: return False
            if node.data<curr.data:
                if not curr.left:
                    curr.left=node
                    return True
                curr=curr.left
            elif node.data>curr.data:
                if not curr.right:
                    curr.right=node
                    return True
                curr=curr.right
            
    def dfs_inorder(self):
        result=[]
        def traverse(curr):
            if curr.left is not None:
                traverse(curr.left)
            result.append(curr.data)
            if curr.right is not None:
                traverse(curr.right)
        traverse(self.root)
        return result
    
    def is_balanced(self):
        def balanced(root):
            if not root:
                return True
            lheight=self.height(root.left)
            rheight=self.height(root.right)
            # Both left and right sub trees(recursively) have to be balanced
            return abs(lheight-rheight)<=1 and balanced(root.left) and balanced(root.right)
        return balanced(self.root)
    
    def height(self,root):
        if not root: return -1
        return 1+max(self.height(root.left),self.height(root.right))
        
    
if __name__=='__main__':
    tree=Tree(4)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(6)
    # print(tree.max_depth())
    # print(tree.dfs_inorder())
    print(tree.is_balanced())
'''
230. Kth Smallest Element in a BST (Medium)
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self,data):
        self.root=Node(data)

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
    
    def kth_element(self,k):
        result=[]
        def traverse(curr):
            if curr.left is not None:
                traverse(curr.left)
            result.append(curr.data)
            if len(result)==k:
                return result
            if curr.right is not None:
                traverse(curr.right)
            return result
        return traverse(self.root)[k-1]

if __name__=='__main__':
    tree=Tree(4)
    tree.insert(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    tree.insert(7)
    tree.insert(9)
    print(tree.kth_element(2))
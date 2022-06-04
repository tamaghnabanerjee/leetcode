'''
104. Maximum Depth of Binary Tree (Easy)
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
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
    
    def max_depth(self):
        def traverse(curr):
            if not curr: return -1
            return 1+max(traverse(curr.left),traverse(curr.right))
        return traverse(self.root)
    
if __name__=='__main__':
    tree=Tree(4)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    tree.insert(7)
    tree.insert(9)
    print(tree.max_depth())
    # print(tree.dfs_inorder())
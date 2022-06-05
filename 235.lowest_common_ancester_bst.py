'''
235. Lowest Common Ancestor of a Binary Search Tree (Easy)
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
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

    def lowest_common_ancester(self,val1,val2):
        node1=Node(val1)
        node2=Node(val2)
        curr=self.root
        while curr:
            if node1.data<curr.data and node2.data<curr.data:
                curr=curr.left
            elif node1.data>curr.data and node2.data>curr.data:
                curr=curr.right
            # nodes are on either side of curr. LCA-> curr
            return curr.data

if __name__=='__main__':
    tree1=Tree(6)
    tree1.insert(2)
    tree1.insert(8)
    tree1.insert(0)
    tree1.insert(4)
    tree1.insert(7)
    tree1.insert(9)
    tree1.insert(3)
    tree1.insert(5)
    # print(tree1.dfs_inorder())
    print(tree1.lowest_common_ancester(2,8))
    
'''
206. Reverse Linked List (Easy)
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        
    def insert(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            node=Node(value)
            self.tail.next=node
            self.tail=node
        return self.head  
            
    def print_list(self):
        if self.head==None:
            return None
        curr=self.head
        while curr:
            print(curr.value)
            curr=curr.next

    def reverse(self):
        if self.head==None:
            return None
        prev=None
        curr=self.head
        self.head=self.tail
        self.tail=curr
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return self.head

if __name__=='__main__':
    linked_list=LinkedList(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)
    linked_list.insert(50)
    linked_list.reverse()
    linked_list.print_list()
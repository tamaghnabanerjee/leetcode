'''
141. Linked List Cycle (Easy)
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
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

    def has_cycle(self):
        curr=self.head
        visited=set()
        while curr:
            if curr in visited:
                return True
            else:
                visited.add(curr)
            curr=curr.next
        return False
  
if __name__=='__main__':
    linked_list=LinkedList(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)
    linked_list.insert(50)
    print(linked_list.has_cycle())

    
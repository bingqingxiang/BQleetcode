# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x 
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0) # creat an empety list node with val init to 0
        result=head # let result point to head 
        carry=0 # init the carry value to 0
       
        while l1 or l2 or carry==1: #if l1 or l2 exist or carry==1
            cur=0 # current value
            if l1:
                cur+=l1.val
                l1=l1.next # let l1 point to the next value
            if l2:
                cur+=l2.val
                l2=l2.next  # let l2 point to the next value
            print(cur)
            cur+=carry # add the carry
            head.next=ListNode(cur % 10) # creat the node with current addition result
            carry= int(cur/10) # calculate the carry for next 
            head=head.next # update head
        
        return result.next   # point to the node contain the last number in the result
        
"""        
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

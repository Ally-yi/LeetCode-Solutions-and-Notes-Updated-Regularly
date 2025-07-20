"""
Problem: Add Two Numbers (LeetCode #2)
Link: https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a = ListNode()
        current = a
        carry = 0
        while l1 or l2 or carry:
            ll1 = l1.val if l1 else 0
            ll2 = l2.val if l2 else 0
            newValue = (ll1 + ll2 + carry) % 10
            carry = (ll1 + ll2 + carry) // 10
            current.next = ListNode(newValue)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return a.next

# Helper function: Convert a list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode()          
    current = dummy             
    for val in lst:
        current.next = ListNode(val)  
        current = current.next  
    return dummy.next         

# Helper function: Convert a singly linked list to a Python list (for printing or testing)
def linkedlist_to_list(node):
    result = []             
    while node:
        result.append(node.val) 
        node = node.next       
    return result              


# test
if __name__ == "__main__":
    l1 = list_to_linkedlist([2, 4, 3])  
    l2 = list_to_linkedlist([5, 6, 4])  

    sol = Solution()
    result_node = sol.addTwoNumbers(l1, l2)
    result_list = linkedlist_to_list(result_node)

    print(result_list)  # output: [7, 0, 8]

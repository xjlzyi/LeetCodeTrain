# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        cur = head
        m = 0
        delNode = head
        while (cur != None):
            if m > n:
                delNode = delNode.next
            else:
                m += 1
            cur = cur.next
        if m == n and delNode == head:
            return head.next
        else:
            delNode.next = delNode.next.next
        return head
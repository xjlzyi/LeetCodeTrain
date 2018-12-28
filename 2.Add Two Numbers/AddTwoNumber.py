class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    node = head = ListNode(0)
    carry = 0
    while l1 != None or l2 != None or carry == 1:
        sum = carry
        if l1 != None:
            sum += l1.val
            l1 = l1.next
        if l2 != None:
            sum += l2.val
            l2 = l2.next
        carry = sum // 10
        node.next = ListNode(sum % 10)
        node = node.next
    return head.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(3)
l2.next = ListNode(6)
l2.next = ListNode(5)
print(addTwoNumbers(l1, l2))

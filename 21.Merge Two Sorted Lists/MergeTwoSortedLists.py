class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		head = temp = ListNode(0)	
		while l1 != None and l2 != None:
			if l1.val < l2.val:
				temp.next = l1
				l1 = l1.next
			else:
				temp.next = l2
				l2 = l2.next
			temp = temp.next
		temp.next = l1 or l2
		return head.next
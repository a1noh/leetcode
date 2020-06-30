# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while (fast is not None and fast.next is not None):
            slow = fast.next
            fast = fast.next.next
        slow = self.reverse(slow)
        fast = head
        while slow is not None:
            if slow.val is not fast.val:
                print("F")
                return
            else:
                slow = slow.next
                fast = fast.next
        print("T")

    def reverse(self, head: ListNode) -> ListNode:
        ll = None
        nex = None
        while (head != None):
            nex = head.next
            head.next = ll
            ll = head
            head = nex
        return ll


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)


Solution().isPalindrome(head)

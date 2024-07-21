from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """
            This is to String method.
        """
        str2 = str(self.val)
        temp = self.next
        while temp:
            str2 = str2 + ", " + str(temp.val)
            temp = temp.next

        return str2
    
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        answer = ListNode()
        prev = answer

        while l1 or l2 or carry > 0:
            if l1:
                carry += l1.val
                l1 = l1.next          
            if l2:
                carry += l2.val
                l2 = l2.next

            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry = carry //10

        return answer.next

sln = Solution()
# l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
# l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
l1 = ListNode(1, ListNode(8))
l2 = ListNode(0)

print(sln.addTwoNumbers(l1, l2))
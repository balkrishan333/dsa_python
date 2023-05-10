from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        str2 = str(self.val)
        temp = self.next
        while temp:
            str2 = str2 + ", " + str(temp.val)
            temp = temp.next

        return str2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0; answer = None; prev = None

        while l1 and l2:
            sum = l1.val + l2.val + carry
            val = sum % 10
            carry = sum // 10
            l3 = ListNode(val)

            if answer is None:
                answer = l3
            else:
                prev.next = l3

            prev = l3
            l1 = l1.next
            l2 = l2.next

        leftover = None
        if l1:
            leftover = l1

        if l2:
            leftover = l2

        while leftover:
            if carry == 1 and leftover.val == 9:
                prev.next = ListNode(0)
            else:
                prev.next = ListNode(leftover.val+carry)
                carry = 0

            prev = prev.next
            leftover = leftover.next

        if carry == 1:
            prev.next = ListNode(carry)

        return answer

sln = Solution()
# l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
# l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
l1 = ListNode(1, ListNode(8))
l2 = ListNode(0)

print(sln.addTwoNumbers(l1, l2))
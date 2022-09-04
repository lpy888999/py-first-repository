class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = cur = ListNode()
        remainder = 0 #进位
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + remainder
            cur.next = ListNode(sum%10) #创建新节点
            remainder = sum // 10  # //整除 /浮点数
            #不空往下走
            if l1:l1 = l1.next 
            if l2:l2 = l2.next 

            cur = cur.next #result 也往后走
        if remainder:cur.next=ListNode(remainder) 
        return result.next


from asyncio.windows_events import NULL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    p = list1
    q = list2
    newhead = ListNode(0)
    cur = newhead
    while p and q:    
        if p.val >= q.val:
            cur.next = q
            cur = cur.next
            q = q.next
        else:
            cur.next = p
            cur = cur.next
            p = p.next
    if p == None: #剩下的直接添至尾部
        cur.next = q
    if q == None:
        cur.next = p
            
    return newhead.next

         
#递归？
  
    
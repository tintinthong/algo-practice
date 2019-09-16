class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        
        nodel1 , nodel2= l1 , l2
        nodel3=ListNode(nodel1.val+nodel2.val)
        result=nodel3
        print(nodel1.val, nodel2.val, nodel3.val)

        while (nodel1.next !=None and nodel2.next !=None):
            nodel3.next=ListNode(nodel1.next.val+nodel2.next.val)
            nodel1, nodel2, nodel3=nodel1.next , nodel2.next ,nodel3.next
            print(nodel1.val, nodel2.val, nodel3.val)
        return result 

l1 = ListNode(5)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

##### Solution #####
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val,)
    result = result.next

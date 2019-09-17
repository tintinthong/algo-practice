class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += ""
            node = node.next
        print(output)

    def reverseIteratively(self, head):

        prevnode = None
        node = head
        nextnode = node.next
        node.next=prevnode

        while nextnode != None:
            prevnode = node
            node = nextnode 
            nextnode = node.next
            node.next=prevnode

    def reverseRecursively(self, head):
        print('whatever')



# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
print('----')
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4

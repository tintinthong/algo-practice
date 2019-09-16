class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):

    def goingdown(node):
            values.append(node.value)
            if(not node.right and not node.left):
                return
            if(node.right):
                goingdown(node.right)
            if(node.left):
                goingdown(node.left)

    # ceiling is larger than or equal to k
    def findinf(sortedvalues, k):
        i = 0
        while(sortedvalues[i] <= k):
            inf = values[i]
            i = i+1
        return(inf)


    # floor is less than or equal to k
    def findsup(sortedvalues, k):
        i = 0
        sortedvalues.reverse()
        while(sortedvalues[i] >= k):
            sup = sortedvalues[i]
            i = i+1
        return(sup)

    values = []
    goingdown(root)
    values.sort()
    return([findinf(values, 5),findsup(values, 5)])
    
root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)

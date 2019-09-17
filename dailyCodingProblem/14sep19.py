
def twonumbersum(numberlist,k):
    for i in range(0,len(numberlist)):
        for j in range(0,len(numberlist)):
            print(i,j)
            if(i!=j):
                if(numberlist[i]+numberlist[j]==k):
                    return True
    return False

print(twonumbersum([1,2,5],7))
# convert s2 to s1
def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        # more characters of s2 will be deleted
        return len(s2)-index2
    if index2 == len(s2):
        # more characters of s1 will be addeed to s2
        return len(s1)-index1
    
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    else:
        # deleteing one value of s2
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1)
        # inserting one value to s2
        insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        # replacing one value of s2
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tble", 0, 0))
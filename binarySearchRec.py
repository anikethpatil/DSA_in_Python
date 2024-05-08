def binarySearchRec(arr,p,l,h):
    mid=(l+h)//2
    if l>h:
        return False
    else:
        if arr[mid]==p:
            return mid
        elif p<arr[mid]:
            return binarySearchRec(arr,p,l,mid-1)
        else:
            return binarySearchRec(arr,p,mid+1,h)
if __name__=='__main__':
    array=[4,5,6,7,8]
    q=binarySearchRec(array,8,0,len(array)-1)
    if q==False:
        print("Not Found")
    else:
        print("Found at position",q)

'''
best case=O(n)
worst case=O(logn)
'''
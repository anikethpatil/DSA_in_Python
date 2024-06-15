def binarySearch(arr,p,l,h):
    while l<=h:
        mid = (l+h)//2
        if arr[mid]==p:
            return mid
        elif arr[mid]<p:
            l=mid+1
        else:
            h=mid-1
    return -1

if __name__=='__main__':
    array=[1,2,4,6,8]
    y=binarySearch(array,8,0,len(array)-1)
    if y==-1:
        print("Not Found")
    else:
        print("Found at position",y)

'''
best case=O(1)
worst case=O(logn)

'''

def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
if __name__=='__main__':
    values=[5,4,2,1,3]
    insertionSort(values)
    print(values)
'''
best case:O(n)
worst case:n*(n-1) ~ O(n^2)
space complexity:O(1)

when there are only a few elements left to be sorted
'''
def swap(a,b,arr):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    
def partition(array,l,h):
    pivot_index=l
    pivot=array[pivot_index]

    i=pivot_index+1
    j=len(array)-1

    while i<j:
        while i<len(array) and array[i]<=pivot:
            i=i+1
        while array[j]>pivot:
            j=j-1
        if i<j:
            swap(i,j,array)
    swap(pivot_index,j,array)

    return j

def quickSort(array,l,h):
    if l<h:
        pi=partition(array,l,h)
        quickSort(array,l,pi-1)
        quickSort(array,pi+1,h)

if __name__=='__main__':
    array=[5,1,2,3,4]
    quickSort(array,0,len(array)-1)
    print(array)
        
'''
best case=O(nlogn)
average case=O(nlogn)
worst case=O(n^2)
'''

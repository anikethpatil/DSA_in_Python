def mergeSort(array):
    if len(array)==0:
        print("Empty")
        exit()
    
    if len(array)>1:
        r=len(array)//2
        L=array[:r]
        M=array[r:]
        mergeSort(L)
        mergeSort(M)
        i=j=k=0
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i=i+1
            else:
                array[k]=M[j]
                j=j+1
            k=k+1
        while i<len(L):
            array[k]=L[i]
            i=i+1
            k=k+1
        while j<len(M):
            array[k]=M[j]
            j=j+1
            k=k+1
def printArray(array):
    for i in range(len(array)):
        print(array[i])
        

if __name__=='__main__':
    array=[3,2,5,1,7]
    mergeSort(array)
    
    printArray(array)

'''
best case=O(nlogn)
worst case=O(nlogn)
average case=O(nlogn)    
'''
        


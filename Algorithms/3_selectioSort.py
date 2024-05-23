def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        (arr[i],arr[min])=(arr[min],arr[i])
    return arr

if __name__=='__main__':
    values=[5,4,2,3,1]
    selectionSort(values)
    print(values)

'''
best case:O(n^2)
worst case:O(n^2)
space complexity:O(1)

flash memory (number of writes/swaps is O(n) as compared to O(n^2) of bubble sort)
'''
def bubbleSort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swapped=True
            
        if swapped==False:
            break
    return arr

if __name__=='__main__':
    values=[5,2,4,3,6]
    bubbleSort(values)
    print(values)

'''
best case=O(n)
worst case=O(n^2)
space complexity=O(2)
'''

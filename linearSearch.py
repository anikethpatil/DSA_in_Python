def linearSearch(p,n,arr):
    for i in range(0,n):
        if arr[i]==p:
            return i
    return -1

if __name__=='__main__':
    array=[1,2,3,4,5]
    y=linearSearch(20,len(array),array)
    if y==-1:
        print("Not Found!!")
    else:
        print("Found at position",y)
        
'''
Time complexity=O(n)
'''
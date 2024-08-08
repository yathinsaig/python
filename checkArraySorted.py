def checkArraySort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                return False
            
        return True

arr = [2,1,3,4,5,6]
n = 6
print(checkArraySort(arr,n))
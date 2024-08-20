def Selection_sort(arr):
    print("Original array ->",arr)
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    
    return arr

arr = [45,5,34,20,19,9]
a = Selection_sort([100,90,40,30,80,10])
print("Selection sort ->",a)
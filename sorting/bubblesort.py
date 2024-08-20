def Bubble_sort(arr):
    print("Original array ->",arr)
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

arr = [56,44,40,30,28,25]
a = Bubble_sort(arr)
print("Bubble sort ->",a)
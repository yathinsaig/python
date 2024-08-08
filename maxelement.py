def MaxElement(arr, n):
    max = arr[0]
    for i in range(0,n):
        if arr[i] > max:
            max = arr[i]
    return max

arr1 = [5,2,4,5,6,8]
arr2 = [33,55,44,22,11,9]
n = 6
max = MaxElement(arr1, n)
print(MaxElement(arr2,n))
print(max)

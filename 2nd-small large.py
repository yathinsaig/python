
def SecondLargest(arr,n):
    large = arr[0]
    for i in range(n):
        if arr[i] > large:
            SecondLarge = large
            large = arr[i]
    return SecondLarge

def SecondSmallest(arr,n):
    small = float('inf')
    SecondSmall = float('inf')

    for i in range(n):
        if arr[i] < small:
            SecondSmall = small
            small = arr[i]
        elif arr[i] < SecondSmall and arr[i] != small:
            SecondSmall = arr[i]
    return SecondSmall


arr = [2,3,4,5,6,7] #2ndLarge = 6, small = 3
arr1 = [9,8,10,4,11,7] #2ndLarge = 10, small = 7 
n = 6
print(SecondLargest(arr,n))
print(SecondLargest(arr1,n))
print(SecondSmallest(arr,n))
print(SecondSmallest(arr1,n))


    

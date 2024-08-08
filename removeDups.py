# def RemoveDuplicates(arr):
#     i = 0
#     for j in range(i+1,len(arr)):
#         if arr[i] != arr[j]:
#             i += 1
#             arr[i] = arr[j]
#     return i+1

# arr = [  1,1,6,6,6,2,2,2,3,3,4,4]
# n = RemoveDuplicates(arr)
# for i in range(n):
#     print(arr[i],end=" ")


def Remove(arr):
    result = []

    for i in range(len(arr)):
        if arr[i] in result:
            continue
        else:
            result.append(arr[i])

    return sorted(result)

print(Remove([1,33,44,33,55,33,66,7,7,8]))


def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linearsearch([1,2,3,4,5],5))

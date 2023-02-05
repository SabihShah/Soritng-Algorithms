def insertion(arr):
 
    for i in range(1, len(arr)):
 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
arr = [5, 64, 89, 1, 6, 100, 74, 2]
insertion(arr)
for i in range(len(arr)):
    print ("% d" % arr[i], end=" ")
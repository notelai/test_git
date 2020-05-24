def bubble_sort(arr) : 
for j in range(i+1,n):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
return arr

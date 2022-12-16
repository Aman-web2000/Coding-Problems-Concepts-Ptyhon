def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        is_sorted=True
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if is_sorted:
            break
    return arr

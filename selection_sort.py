def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                min_idx=j
        if min_idx!=i:
            arr[min_idx],arr[i]=arr[i],arr[min_idx]
    return arr

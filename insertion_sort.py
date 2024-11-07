def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
        
    return arr

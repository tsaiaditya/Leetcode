def countSort(arr):
    maxval = max(arr) 
    minval = min(arr) 
    range = max - min + 1
      
    count, output = [],[] 
    for i in range(len(arr)): 
        count[arr[i]-min]+=1 
          
    for i in range(len(count)): 
           count[i] += count[i-1]
    
    for i in range(len(arr)-1,-1,-1):
        output[ count[arr[i]-min] -1 ] = arr[i]
        count[arr[i]-min]-=1

    for i in range(len(arr)):
            arr[i] = output[i]
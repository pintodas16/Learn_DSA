def helper(arr, subset, ans, i ):
    
    if i == len(arr):
        ans.append(subset[:])
        return
    
    
    subset.append(arr[i])
    helper(arr, subset,ans,i+1)
    subset.pop()
    # print(i,len(arr))
    # skip the element 
    while (i+1)<len(arr) & arr[i] == arr[i+1]:
        i+=1
        
    helper(arr,subset,ans, i+1)
    
    
arr = list(map(int,input().split()))
arr.sort()
ans = []
subset = []
helper(arr,subset,ans,0)
print(ans)
    
        
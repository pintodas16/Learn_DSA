
def helper(arr, subset , ans , i ):
    
    if i == len(arr):
        ans.append(subset[:])
        return 
    # take the element 
    subset.append(arr[i])
    helper(arr, subset, ans , i+1)
    
    subset.pop()   #backtracking 
    # skip the element 
    helper(arr, subset, ans , i+1)
    



arr = list(map(int,input().split()))
ans = []
subset = []
helper(arr, subset,ans,  0)
print(ans)
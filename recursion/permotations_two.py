def is_check_present(arr,start,curr):
    for i in range(start,curr):
        if arr[i] == arr[curr]:
            return False
    return True

def permu(arr,pos,ans):
    
    if pos == len(arr):
        # print(arr)
        ans.append(arr[:])
        
        return 
    for i in range(pos,len(arr)):
        if is_check_present(arr,pos,i):
            arr[i],arr[pos] = arr[pos],arr[i]
            permu(arr,pos+1,ans)
            arr[i],arr[pos] = arr[pos],arr[i]
 
arr = list(map(int,input().split()))
ans = []
permu(arr,0 ,ans)
print(ans)





from copy import copy
def helper (arr, i , sub , ans, k, sum ):
    # if i == len(arr):
    #     return
    # if sum == k :
    #     ans.append(copy(sub))
    #     return
    # if sum> k :
    #     return
    
    # helper(arr, i+1, sub , ans , k,sum)
    
    
    # sub.append(arr[i])
    # sum += arr[i]
    # helper(arr, i+1 , sub,ans, k ,sum)
    # sum -= arr[i]
    # sub.pop()
    
    
    # if i == len(arr) : return 
    # if sum == k : 
    #     ans.append(sub[:])
    #     return 
    
    # helper(arr, i+1 , sub ,ans , k , sum )
    # count = 0
    # while sum <= k :
    #     count +=1
    #     sub.append(arr[i])
    #     sum += arr[i]
    #     helper(arr, i+1 , sub,ans, k ,sum)
        
       
    # while count:
    #     print('before',end=" ")
    #     print(sub)
    #     sub.pop()
    #     print('after',end=" ")
    #     print(sub)
    #     count -= 1
    
    if k < 0 : 
        return 
    if i == len(arr):
        return 
    if k == 0 :
        ans.append(sub[:])
        return 
    
    
    helper( arr,i+1,  sub , ans, k,sum )
    
    sub.append(arr[i])
    helper(arr, i, sub , ans , k-arr[i],sum)
    sub.pop()


li = list(map(int,input().split()))
k = int(input())
sub = []
ans = []
sum = 0
helper(li,0,sub,ans,k,sum)
print(ans)
# def combination(i,arr,k,ans ,sub):
    
#     if (i >= len(arr)):
#         if (k==0):
#             ans.append(sub[:])
#         return
    
#     # take element 
#     sub.append(arr[i])
#     combination(i+1,arr,k-1,ans,sub)
    
#     # skip the element 
#     sub.pop()
#     combination(i+1,arr, k , ans , sub)

def combination(i,n,k,ans ,sub):
    
    if i > n:
        if (k==0):
            ans.append(sub[:])
        return
    
    # take element 
    sub.append(i)
    combination(i+1,n,k-1,ans,sub)
    
    # skip the element 
    sub.pop()
    combination(i+1,n, k , ans , sub)


n , k = map(int,input().split())
# print(n,k)

arr = []
ans = []
sub = []

for i in range(1,n+1):
    arr.append(i)
# print(arr)
print(len(arr))
combination(1,n,k,ans,sub)
print(ans)



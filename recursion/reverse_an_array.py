def reverse_array(arr, l, r):
    
    if l>=r: return  #bae case  if l is grater or equal r then simply return 
    arr[l],arr[r] = arr[r],arr[l]  #swap the element 
    reverse_array(arr,l+1,r-1)     # call the function 
    
arr = list(map(int,input().split()))

reverse_array(arr,0,len(arr)-1)
print(arr)

# time compolexity O(n)
# space complexity O(n/2) or O(n) because here n/2 swap are done 
# if say constant space complexity then use two pointer method  
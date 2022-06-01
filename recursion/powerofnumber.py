
def power(x,n):
    
    if n==0 : return 1
    partial_ans = power(x,n-1)
    return x*partial_ans


x,n = map(int,input("Enter the base number and power number : ").split())
ans = power(x,n)
print(ans)
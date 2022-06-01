# find the sum of nth natural number . using recursion 

def sum_of(n):
    if n== 1:
        return 1
    partial_ans = sum_of(n-1) 
    return partial_ans + n

n = int(input('Enter a number :'))
ans = sum_of(n)
print(ans)
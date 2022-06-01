
def fibo(n):
    if n==1 or n==2: return 1
    partial_ans_1 = fibo(n-1)
    partial_ans_2 = fibo(n-2)
    return partial_ans_1 + partial_ans_2

n = int(input("please enter n'th term of a number : "))

ans = fibo(n)
print(ans)  #print the n'th term of fibonacci number 


# print the series 
for i in range(1,n+1):
    print(fibo(i))

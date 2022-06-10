


def per(pos , string,ans):
    length = len(string)
    if pos>= length :
        ans.append("".join(string))
        return 
    for i in range(pos,length):
        string[i],string[pos] = string[pos],string[i]
        per(pos+1,string,ans)
        string[i],string[pos] = string[pos],string[i]
        
str = input()
ans = []
string = []
string = list(str)
per(0,string, ans )
print(ans)
        
def factlst(lst):
    for i in lst:
        print(fact(i))

def fact(i):
    ans=1
    if i==0: return 1
    for j in range (1,i+1):
        ans*=j
    return ans


lst=[5,5,5,5,5]
factlst(lst)
def fact(num):
    ans=1
    if num==0: return ans
    for i in range (1,num+1):
        ans*=i
    return ans

num=int(input("Enter the num for calcualting factorial "))
print(fact(num))
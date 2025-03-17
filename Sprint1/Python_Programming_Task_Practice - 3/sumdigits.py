def sumdigits(n):
    while n >= 10:   
        sum=0
        while n > 0 :
            sum+=n%10
            n//=10
        n=sum

    return sum

num = 38
print(sumdigits(num))
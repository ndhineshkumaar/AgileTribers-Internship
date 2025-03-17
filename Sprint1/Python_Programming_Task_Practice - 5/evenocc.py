#as the qs is b/w 10 and 55 these both wont be counted

evencount=0
oddcount=0
for i in range(11,55):
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
print("Even Count " + str(evencount)+"\nOdd Count "+str(oddcount))
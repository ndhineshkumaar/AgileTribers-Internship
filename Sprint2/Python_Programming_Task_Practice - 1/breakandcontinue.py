sum=0
while True:
    num=int(input("Enter the number: "))
    if num<0:
        continue
    elif num==0:
        break
    sum+=num

print("The sum of the numbers is", sum)

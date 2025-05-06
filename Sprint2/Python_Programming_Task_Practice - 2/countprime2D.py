def isprime(number):
    if number<=1:
        return False
    else:
        for i in range (2,int(number**0.5)+1):
            if number%i==0:
                return False
        return True



matrix = [ [2, 4, 5], [7, 9, 11], [13, 16, 19] ]
count=0
for i in range (len(matrix)):
    for j in range (len(matrix[i])):
        if isprime(matrix[i][j]):
            count+=1

print("Total prime numbers: ",count)
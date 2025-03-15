#square

def sqpatter(r,c):
    print("Sqaure\n")
    for i in range(r):
        for j in range(c): 
            print("*", end=" ") 
        print()

sqpatter(3,7)

#triangle

def tripatter(n):
    print("Triangle\n")
    for i in range (n):
        print("*"*(i+1))

tripatter(5)

#diamond

def diapatter(n):
    print("Diamond\n")
    for i in range(1,n+1,2):
        print(" "*((n-i)//2)+"*"*i)
    for i in range(n-2,0,-2): 
        print(" "*((n-i)//2) +"*"*i)

diapatter(7)
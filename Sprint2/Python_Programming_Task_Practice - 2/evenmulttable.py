for i in range (1,11):
    if i % 2 == 0:
        for j in range (1,11):
            if (i*j)%2==0:
                print(f"{i * j:4}", end="")
    print()
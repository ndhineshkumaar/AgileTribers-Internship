set1= {5,6,7,8,3}
set2= {1,2,3,4,5}

print("Union : ", set1 | set2)
print("Intersection : ", set1 & set2)
print("Difference : ", set1 - set2)

set1.add(10)
print(set1)

set2.remove(5)
print(set2)

n=int(input("Enter the number to check on set1: "))
if n in set1:
    print("Yes it is present")
else:
    print("No it is not present")
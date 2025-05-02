list1=[2,3,4,5,3,6,5,4,5,4,5,1,3]
set1=set(list1)

print(set1)

set2={2,5,4,1,9,3,2}

print("Unique Elements from Original Set:",set1-set2)

print("Common Elements from Both Set:",set1 & set2)

print("All Elements from Both Set:",set1 | set2)
def lstavg(lst):
    avg=0
    m=len(lst)
    for i in lst:
        avg+=i
    return float(avg/m)

lst=[3,3,3,3,3]
print(lstavg(lst))
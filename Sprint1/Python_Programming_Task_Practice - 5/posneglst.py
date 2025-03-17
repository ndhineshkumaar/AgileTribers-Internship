def posneglst(lst):
    poslst=[]
    neglst=[]
    for i in lst:
        if i<0: neglst.append(i)
        elif i>0: poslst.append(i)

    return poslst,neglst


lst=[23, 4, -6, 23, -9, 21, 3, -45, -8]
print(posneglst(lst))
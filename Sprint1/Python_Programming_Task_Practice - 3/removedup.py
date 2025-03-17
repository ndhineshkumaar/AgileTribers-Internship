def removedup(lst):
    found=[]
    for i in lst:
        if i not in found:
            found.append(i)
    return found


lst=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print(removedup(lst))
def frstlst(lst):
    if lst[0]==lst[-1]:
        return True
    else:
        return False
    

lst=[10, 20, 30, 40, 10]
print(frstlst(lst))
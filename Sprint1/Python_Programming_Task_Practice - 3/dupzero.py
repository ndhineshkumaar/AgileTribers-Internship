def dupzero(lst):
    l=len(lst)
    i=0
    while i<l:
        if lst[i]==0:
            lst.insert(i+1,0)
            lst.pop()
            i+=1
        i+=1
    return lst

print(dupzero([1,0,2,3,0,4,5,0]))
            
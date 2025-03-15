def commomlst(lst1,lst2):
    ans=set()
    for i in lst1:
        if i in lst2:
            ans.add(i)
    return ans

lst1=[1,2,2,1]
last2=[2,2]
print(commomlst(lst1,last2))
def remandrep(lst,num):
    anslst=[]
    count=0
    for i in lst:
        if i==num:
            count+=1
        else:
            anslst.append(i)

    anslst.extend([0]*count)
    return anslst



lst=[2,3,2,3,3]
remove=3
print(remandrep(lst,remove))
def checkdup(lst):
    dict={}
    for i in lst:
        if i in dict:
            return True
        else:
            dict[i]=1
    return False


nums = [1,2,3,1] 
print(checkdup(nums))
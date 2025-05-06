def merge_dicts(dict1, dict2):
    for i in dict2:
        if i in dict1:
            dict1[i]+=dict2[i]
        else:
           dict1[i]=dict2[i]
    print(dict1)


dict1 = {'apple': 5, 'banana': 3, 'orange': 7}
dict2 = {'banana': 2, 'orange': 3, 'grape': 4} 
merge_dicts(dict1, dict2)
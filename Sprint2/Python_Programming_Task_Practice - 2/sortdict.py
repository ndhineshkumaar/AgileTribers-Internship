marks = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
sorteddict=dict(sorted(marks.items(), key= lambda x:x[1], reverse=True))

print(sorteddict)
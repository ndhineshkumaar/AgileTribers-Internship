words="Hello world hello"
word=words.split()
freq={}

for i in word:
    key=i.lower()
    if key in freq:
        freq[key]+=1
    else:
        freq[key]=1

print(freq)
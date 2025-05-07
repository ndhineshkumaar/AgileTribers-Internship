def read_and_append(filename, text):
    file=open(filename,"r+")
    contents=file.read()
    print(contents)
    file.write(f"\n {text}")
    file.seek(0)
    ucontents=file.read()
    print(ucontents)

filename="data.txt"
text="How are you ?"
read_and_append(filename, text)
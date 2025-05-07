def read_file(filename):
    try:
        file=open(filename,"r")
        content=file.read()
        print(content)
    except FileNotFoundError:
        print("The given file does not exist on the working directory")

read_file("files.txt")
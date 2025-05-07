def readfile():
    file=None
    try:
        file=open("Sprint2\Python_Programming_Task_Practice - 3\data.txt","r")
        content=file.read()
        print(content)
    except FileNotFoundError:
        print("Error: The file 'data.txt' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        if file:
            file.close()
            print("File has been closed.")

readfile()
x = 10

def global_use():
    global x  
    x += 1
    print("Global changed", x)

def local_use():
    x = 5
    print("Local Value", x)

local_use()
print("Global before function call", x)
global_use()

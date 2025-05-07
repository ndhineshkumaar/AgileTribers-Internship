def safe_divide(a, b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    
print(safe_divide(5,0))
print(safe_divide(5,2))
def outer_function():
    def inner_function():
        return 10 / 0

    try:
        result = inner_function()
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Exception caught in outer_function: {e}")

outer_function()

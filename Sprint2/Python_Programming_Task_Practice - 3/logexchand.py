import logging

logging.basicConfig(filename="errorlog.txt",level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        num = int(input("Enter the number: "))
        str_val = input("Enter the str: ")
        strtonum = int(str_val)
        div = num / num
        print(f"The converted int: {strtonum} \nThe ans after dividing is {div}")
    except ZeroDivisionError as e:
        logging.error("Division by zero is not allowed.", exc_info=True)
    except ValueError as e:
        logging.error("Converting given string to int is not possible", exc_info=True)

main()
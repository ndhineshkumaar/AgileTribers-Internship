import random
import string

def genpass(passlength):
    letter=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    passw = [random.choice(letter), random.choice(digits)]
    all_chars = letter + digits + symbols
    passw += random.choices(all_chars, k=passlength - 2)    
    random.shuffle(passw)
    return "".join(passw)

#req user for length

while True:
    try:
        passlength=int(input("Enter the number of character for password (min 8) : "))
        if passlength>=8:
            break
        print("Warning!!! The password should conatin minimum of 8 characters ... ")
    except ValueError:
        print("Entered value must be a number")
print(genpass(passlength))
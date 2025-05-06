matchatrix = [ ["madam", "apple", "racecar"], ["level", "hello", "civic"], ["world","deified", "rotor"] ]
for row in matchatrix:
    for word in row:
        if word == word[::-1]:
            print(word," is a palindrome")
        else:
            print(word," is not a palindrome")
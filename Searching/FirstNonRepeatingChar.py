def firstNonRepeatingChar(my_string):
    chars = {}
    for c in my_string:
        if chars.get(c):
            chars[c] += 1
        else:
            chars[c] = 1
    for c in my_string:
        if chars[c] == 1:
            return c
    return "_"

print(firstNonRepeatingChar('akshaytiwari'))
print(firstNonRepeatingChar('codingisfun'))
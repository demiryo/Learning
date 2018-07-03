def incrypt(shift, input_string):
    ret = ""
    input_string = input_string.upper()
    for c in input_string:
        new_ascii = ord(c)+shift
        if new_ascii > 90:
            new_ascii = new_ascii - 26
        ret = ret + chr(new_ascii)
    return ret
def decypt(shift, input_string):
    ret = ""
    input_string = input_string.upper()
    for c in input_string:
        new_ascii = ord(c) - shift
        if new_ascii < 65:
            new_ascii = new_ascii + 26
        ret = ret + chr(new_ascii)
    return ret

print decypt(1, incrypt(1, "Tesz"))
print decypt(2, incrypt(2, "Tesz"))
print decypt(3, incrypt(3, "Tesz"))
print decypt(4, incrypt(4, "Tesz"))
print decypt(5, incrypt(5, "Tesz"))
print decypt(6, incrypt(6, "Tesz"))
print decypt(7, incrypt(7, "Tesz"))

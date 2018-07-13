


input_string = (raw_input(" input words =  "))

def is_alphabet_character(c):
    ascii_c = ord(c)
    ascii_a = ord('A')
    ascii_z = ord('Z')
    return ascii_a <= ascii_c and ascii_c <= ascii_z


def incrypt(shift, input_string):
    ret = ""
    input_string = input_string.upper()
    for c in input_string:
        if is_alphabet_character(c):
            new_ascii = ord(c)+shift
            if new_ascii > 90:
                new_ascii = new_ascii - 26
            ret = ret + chr(new_ascii)
        else:
            ret = ret + c
    return ret
def decypt(shift, input_string):
    ret = ""
    input_string = input_string.upper()
    for c in input_string:
        if is_alphabet_character(c):
            new_ascii = ord(c) - shift
            if new_ascii < 65:
                new_ascii = new_ascii + 26
            ret = ret + chr(new_ascii)
        else:
            ret = ret + c
    return ret

for char in input_string.upper():
    print "is '{}' an alpha {}".format(char, is_alphabet_character(char))

print incrypt(1, input_string)
print ("decription")
print decypt(1 , incrypt(1, input_string) )
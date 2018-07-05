


input_string = (raw_input(" input words =  "))

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


print incrypt(1, input_string)
print ("decription")
print decypt(1 , incrypt(1, input_string) )
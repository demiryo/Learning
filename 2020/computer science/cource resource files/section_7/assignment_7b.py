# This program uses a for loop inside of another for loop.
# You don't need to know what every line of code does to figure
# out what the program is doing.
# Try running the program a few times with different input
# to observe what the program does.
# Use those observations to help you figure out what the program
# does.

# The word variable is: 
word = input("Enter a word: ")
# The length variable is: 
length = len(word)

# The range argument is equal to: 
for i in range(length):
    # The range argument is equal to: 
    for j in range(length):
        # The sum_var variable is: 
        sum_var = i + j
        # If the sum_var variable's value is greater than or
        # equal to the value assigned to length, then sum_var
        # is assigned to the value of sum_var minus the
        # value of length.
        if sum_var >= length:
            sum_var = sum_var - length
        # Print a character slice of the variable word, and then
        # end= adds a space to the end of it.
        print(word[sum_var], end=" ")
    # print() without an argument prints a blank line. 
    print()

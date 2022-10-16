# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#
# Suppose the following input is supplied to the program:
#
# Hello world
# Practice makes perfect
# Then, the output should be:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT

cap_list = []
while True:
    line = input('Enter line')
    if line:
        cap_list.append(line.upper())
    else:
        break
for i in cap_list:
    print(i)
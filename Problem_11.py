# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#
# Example:
#
# 0100,0011,1010,1001
# Then the output should be:
#
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

#VERSION 1
bin_nums = input('Enter Binary Numbers separated by commas').split(',')
output_list = []
for i in bin_nums:
    if int(i, 2)%5 == 0:
        output_list.append(i)
print(output_list)


# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

valid_list = []

start_list = [num for num in range(1000,3001)]
for num in start_list:
    num_char_list = list(str(num))
    print(type(num_char_list[0]))
    if int(num_char_list[0])%2 == int(num_char_list[1])%2 == int(num_char_list[2])%2 == int(num_char_list[3])%2 ==0:
        valid_list.append(num)
print(valid_list)

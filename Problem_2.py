#Write a program which can compute the factorial
#of a given numbers.The results should be printed in a
#comma-separated sequence on a single line.Suppose the
# following input is supplied to the program:
#8 Then, the output should be:40320
import sys
number = sys.argv[1]
def factorial(num):
    result = 1
    for n in range(1, int(num)+1):
        result = result*n
    return result
print(factorial(number))
#Write a program which accepts a sequence of
#comma-separated numbers from console and
#generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:

#34,67,55,33,12,98
#Then, the output should be:

#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
import sys
number_list = sys.argv[1]
def num_converter(num_list):
    l = num_list.split(',')
    t = tuple(l)
    print(l,'\n', t)

num_converter(number_list)
#With a given integral number n, write a program
# to generate a dictionary that contains (i, i x i) such
# that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the
# following input is supplied to the program: 8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# import sys
# number = sys.argv[1]
# def squares_dict(num):
#     d = {}
#     for i in range(1, int(num)+1):
#         d[i] = i**2
#     print(d)
# squares_dict(number)
n = int(input('Choose number'))
d = {num:num**2 for num in range(1, n+1)}
print(d)
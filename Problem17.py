# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
#
# 500
deposits = 0
withdrawals= 0

request = input('>')
while request:
    amount = int(request[1::])
    if request[0] == 'D':
        deposits += amount
    elif request[0] == 'W':
        withdrawals += amount
    request = input('>')
balance = deposits - withdrawals
print(f'Current Balance: {balance}')

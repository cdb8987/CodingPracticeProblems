#Define a class which has at least two methods:

#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class Charlie:
    def __init__(self):
        self.s = ''
    def get_string(self):
        self.str = str(input('Type a String'))
        return str
    def print_upper(self):
        print(self.str.upper())

object = Charlie()
object.get_string()
object.print_upper()
class Father:
    def __new__(self):
        self.__init__ (self)
        print("Father's __new__() invoked")
class Child_Father(Father):
    def __init__(self):
       print("child_Father's__init__) invoked")
def main():
    obji = Child_Father ()
main()
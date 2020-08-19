
import sys

def printName():
    FirstName  = sys.argv[1]
    LastName = sys.argv[2]
    print("Hello my name is {},{}".format(LastName,FirstName))


if __name__ == "__main__":
    printName()

import sys

def printName():
    name  = sys.argv[1]
    print("Hello my name is {}".format(name))


if __name__ == "__main__":
    printName()
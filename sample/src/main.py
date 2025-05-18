from normal import normal
from red import red
import sys

def main():
    args = sys.argv
    if args[1] == "--red" or args[1] == "-r":
        print("Red Image Processing")
        red()
    if args[1] == "--normal" or args[1] == "-n":
        print("Normal Image Processing")
        normal()

if __name__ == "__main__":
    main()

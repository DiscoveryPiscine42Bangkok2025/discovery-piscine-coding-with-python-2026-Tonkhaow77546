import sys
import os
from checkmate import checkmate

def main():
    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                board = f.read()
                print(checkmate(board))
        except (FileNotFoundError, IOError):
            print("Error")

if __name__ == "__main__":
    main()
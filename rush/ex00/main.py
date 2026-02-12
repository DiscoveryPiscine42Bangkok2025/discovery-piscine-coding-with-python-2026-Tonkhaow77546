from checkmate import checkmate

def main():
    # Test Case 1: Rook ยิง King (Success)
    board1 = """\
R...
.K..
..P.
...."""
    
    # Test Case 2: King ปลอดภัย (Fail)
    board2 = """\
..
.K"""

    # Test Case 3: Bishop ยิง King (Success)
    board3 = """\
B...
.K..
....
...."""

    # Test Case 4: มีตัวบัง (Fail)
    board4 = """\
B...
.P..
..K.
...."""

    print(f"Board 1 (Expect Success): {checkmate(board1)}")
    print(f"Board 2 (Expect Fail):    {checkmate(board2)}")
    print(f"Board 3 (Expect Success): {checkmate(board3)}")
    print(f"Board 4 (Expect Fail):    {checkmate(board4)}")

if __name__ == "__main__":
    main()
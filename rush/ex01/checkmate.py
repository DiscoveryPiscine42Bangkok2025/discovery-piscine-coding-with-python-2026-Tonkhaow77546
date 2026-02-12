def check_square_board(board: str) -> int:
    if not board:
        return 0

    lines = [line for line in board.split("\n") if line]
    if not lines:
        return 0
    

    size = len(lines[0])
    valid = all(len(line) == size for line in lines) and len(lines) == size
    return size if valid else 0

def get_all_pos(board_lines: list[str], piece: str) -> list[tuple[int, int]]:
    positions = []
    for y, line in enumerate(board_lines):
        for x, char in enumerate(line):
            if char == piece:
                positions.append((x, y))
    return positions

def ray(board_lines: list[str], x0: int, y0: int, dx: int, dy: int, size: int) -> list[tuple[int, int]]:
    moves = []
    x, y = x0, y0
    while True:
        x += dx
        y += dy
        if not (0 <= x < size and 0 <= y < size):
            break
        moves.append((x, y))
        if board_lines[y][x] != ".":
            break
    return moves

def get_possible_pawn_moves(x: int, y: int, size: int) -> list[tuple[int, int]]:
    moves = []
    if x - 1 >= 0 and y - 1 >= 0:
        moves.append((x - 1, y - 1))
    if x + 1 < size and y - 1 >= 0:
        moves.append((x + 1, y - 1))
    return moves

def checkmate(board: str) -> str:
    size = check_square_board(board)
    if size == 0:
        return "Error"

    lines = [line for line in board.split("\n") if line]

    king_pos_list = get_all_pos(lines, "K")
    if len(king_pos_list) != 1: 
        return "Error"
    king_pos = king_pos_list[0]

    all_danger_moves = set()

    # 1. Check Pawns (P)
    for px, py in get_all_pos(lines, "P"):
        for mx, my in get_possible_pawn_moves(px, py, size):
            all_danger_moves.add((mx, my))

    # 2. Check Rooks (R) 
    for rx, ry in get_all_pos(lines, "R"):
        # บน, ล่าง, ซ้าย, ขวา
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            for move in ray(lines, rx, ry, dx, dy, size):
                all_danger_moves.add(move)

    # 3. Check Bishops (B) 
    for bx, by in get_all_pos(lines, "B"):
        for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            for move in ray(lines, bx, by, dx, dy, size):
                all_danger_moves.add(move)

    # 4. Check Queens (Q) 
    for qx, qy in get_all_pos(lines, "Q"):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        for dx, dy in directions:
            for move in ray(lines, qx, qy, dx, dy, size):
                all_danger_moves.add(move)

    if king_pos in all_danger_moves:
        return "Success"
    else:
        return "Fail"
def check_square_board(board: str) -> int:
    if not board:
        return 0
    # ลบ space หรือ newline ส่วนเกินออกก่อนเช็ค
    lines = [line for line in board.split("\n") if line]
    if not lines:
        return 0
        
    size = len(lines[0])
    # เช็คว่าทุกบรรทัดยาวเท่ากัน และ จำนวนบรรทัดเท่ากับความยาว (จัตุรัส)
    valid = all(len(line) == size for line in lines) and len(lines) == size
    return size if valid else 0

def get_all_pos(board_lines: list[str], piece: str) -> list[tuple[int, int]]:
    """หาตำแหน่งของหมาก 'ทุกตัว' ที่เป็นประเภทนั้นๆ"""
    positions = []
    for y, line in enumerate(board_lines):
        for x, char in enumerate(line):
            if char == piece:
                positions.append((x, y))
    return positions

def ray(board_lines: list[str], x0: int, y0: int, dx: int, dy: int, size: int) -> list[tuple[int, int]]:
    """ยิง Ray ไปจนกว่าจะตกขอบหรือชนหมากตัวอื่น"""
    moves = []
    x, y = x0, y0
    while True:
        x += dx
        y += dy
        if not (0 <= x < size and 0 <= y < size):
            break
        moves.append((x, y))
        # ถ้าเจอตัวอะไรก็ตามที่ไม่ใช่จุด ให้หยุด (กินได้ตัวนี้ตัวสุดท้าย หรือโดนบล็อก)
        if board_lines[y][x] != ".":
            break
    return moves

def get_possible_pawn_moves(x: int, y: int, size: int) -> list[tuple[int, int]]:
    # Pawn กินทแยงขึ้นบนซ้ายและขวา
    moves = []
    # เช็คว่ากินซ้ายบนได้ไหม
    if x - 1 >= 0 and y - 1 >= 0:
        moves.append((x - 1, y - 1))
    # เช็คว่ากินขวาบนได้ไหม
    if x + 1 < size and y - 1 >= 0:
        moves.append((x + 1, y - 1))
    return moves

def checkmate(board: str) -> str:
    size = check_square_board(board)
    if size == 0:
        return "Error"  # โจทย์ให้ print Error ถ้ากระดานผิด

    lines = [line for line in board.split("\n") if line]
    
    # หา King
    king_pos_list = get_all_pos(lines, "K")
    if len(king_pos_list) != 1: 
        return "Error" # ต้องมี King 1 ตัวเท่านั้น
    king_pos = king_pos_list[0]

    all_danger_moves = set() # ใช้ set เพื่อความเร็วและตัดตัวซ้ำ

    # 1. Check Pawns (P)
    prawn_pos_list = get_all_pos(lines, "P")
    if len(prawn_pos_list) > 8:
        return "Error" # ต้องมี prawn ไม่เกิน 8 ตัว
    for px, py in get_all_pos(lines, "P"):
        for mx, my in get_possible_pawn_moves(px, py, size):
            all_danger_moves.add((mx, my))

    # 2. Check Rooks (R) - ใช้ Ray เหมือน Queen แต่ออก 4 ทิศ
    rook_pos_list = get_all_pos(lines, "R")
    if len(rook_pos_list) > 2:
        return "Error" # ต้องมี rook ไม่เกิน 2 ตัวเท่านั้น
    for rx, ry in get_all_pos(lines, "R"):
        # บน, ล่าง, ซ้าย, ขวา
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            for move in ray(lines, rx, ry, dx, dy, size):
                all_danger_moves.add(move)

    # 3. Check Bishops (B) - 4 ทิศทแยง
    bishop_pos_list = get_all_pos(lines, "B")
    if len(bishop_pos_list) > 2:
        return "Error" # ต้องมี Bishop ไม่เกิน 2 ตัวเท่านั้น
    for bx, by in get_all_pos(lines, "B"):
        for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            for move in ray(lines, bx, by, dx, dy, size):
                all_danger_moves.add(move)

    # 4. Check Queens (Q) - 8 ทิศ
    queen_pos_list = get_all_pos(lines, "Q")
    if len(queen_pos_list) > 1:
        return "Error" # ต้องมี Queen ไม่เกิน 1 ตัวเท่านั้น
    for qx, qy in get_all_pos(lines, "Q"):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        for dx, dy in directions:
            for move in ray(lines, qx, qy, dx, dy, size):
                all_danger_moves.add(move)

    if king_pos in all_danger_moves:
        return "Success"
    else:
        return "Fail"
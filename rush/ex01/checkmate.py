def check_square_board(board: str) -> int:
    """
    Validates if the board is a perfect square (NxN).
    Returns size N if valid, else 0.
    """
    if not board:
        return 0
    
    # Parse board into lines, removing empty strings
    lines = [line for line in board.split("\n") if line]
    if not lines:
        return 0
        
    size = len(lines[0])
    
    # Check consistency: Width == Height for all lines
    valid = all(len(line) == size for line in lines) and len(lines) == size
    return size if valid else 0

def get_all_pos(board_lines: list[str], piece: str) -> list[tuple[int, int]]:
    """
    Scans the grid to find all (x, y) coordinates of a specific piece type.
    """
    positions = []
    for y, line in enumerate(board_lines):
        for x, char in enumerate(line):
            if char == piece:
                positions.append((x, y))
    return positions

def ray(board_lines: list[str], x0: int, y0: int, dx: int, dy: int, size: int) -> list[tuple[int, int]]:
    """
    Simulates linear movement (Ray Casting) for R, B, Q.
    Stops upon hitting board edges or colliding with another piece.
    """
    moves = []
    x, y = x0, y0
    while True:
        x += dx
        y += dy
        
        # Check 1: Boundary check (Stop if out of bounds)
        if not (0 <= x < size and 0 <= y < size):
            break
            
        moves.append((x, y))
        
        # Check 2: Collision detection (Stop if path is blocked)
        if board_lines[y][x] != ".":
            break
            
    return moves

def get_possible_pawn_moves(x: int, y: int, size: int) -> list[tuple[int, int]]:
    """
    Calculates Pawn's capture zones.
    Logic: Pawns attack diagonally upward (Top-Left & Top-Right).
    """
    moves = []
    # Check Top-Left
    if x - 1 >= 0 and y - 1 >= 0:
        moves.append((x - 1, y - 1))
    # Check Top-Right
    if x + 1 < size and y - 1 >= 0:
        moves.append((x + 1, y - 1))
    return moves

def checkmate(board: str) -> str:
    # --- 1. Board Validation ---
    size = check_square_board(board)
    if size == 0:
        return "Error"

    lines = [line for line in board.split("\n") if line]
    
    # --- 2. Piece Validation (King & Queen) ---
    # Ensure exactly one King exists
    king_pos_list = get_all_pos(lines, "K")
    if len(king_pos_list) != 1: 
        return "Error"
    king_pos = king_pos_list[0]

    # Ensure exactly one Queen exists (Optional rule based on previous context)
    queen_pos_list = get_all_pos(lines, "Q")
    if len(queen_pos_list) != 1:
        return "Error"

    # --- 3. Calculate Threat Map (Danger Zone) ---
    # Use a Set to store unique danger coordinates
    all_danger_moves = set()

    # A. Pawn Threats (Diagonal capture)
    for px, py in get_all_pos(lines, "P"):
        for mx, my in get_possible_pawn_moves(px, py, size):
            all_danger_moves.add((mx, my))

    # B. Rook Threats (Horizontal/Vertical Ray Casting)
    for rx, ry in get_all_pos(lines, "R"):
        # Directions: Up, Down, Left, Right
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            for move in ray(lines, rx, ry, dx, dy, size):
                all_danger_moves.add(move)

    # C. Bishop Threats (Diagonal Ray Casting)
    for bx, by in get_all_pos(lines, "B"):
        # Directions: 4 Diagonals
        for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            for move in ray(lines, bx, by, dx, dy, size):
                all_danger_moves.add(move)

    # D. Queen Threats (Rook + Bishop movements)
    for qx, qy in queen_pos_list:
        # Directions: All 8 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        for dx, dy in directions:
            for move in ray(lines, qx, qy, dx, dy, size):
                all_danger_moves.add(move)

    # --- 4. Final Check ---
    # If King is inside the danger zone -> Success (Checkmate)
    if king_pos in all_danger_moves:
        return "Success"
    else:
        return "Fail"
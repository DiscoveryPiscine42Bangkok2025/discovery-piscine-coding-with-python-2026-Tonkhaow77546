import sys

# พยายาม import ฟังก์ชัน checkmate
try:
    from checkmate import checkmate
except ImportError:
    print("❌ Error: ไม่พบไฟล์ checkmate.py หรือชื่อฟังก์ชันไม่ถูกต้อง")
    sys.exit(1)

def run_test(name, board, expected):
    """ฟังก์ชันช่วยรันเทสและแสดงผลลัพธ์ให้สวยงาม"""
    # จับ Error กรณีโปรแกรม Crash
    try:
        result = checkmate(board)
    except Exception as e:
        result = f"CRASH ({e})"

    status = "✅ PASS" if result == expected else f"❌ FAIL"
    
    print(f"{status} | {name:<40}")
    
    # ถ้าไม่ผ่าน ให้โชว์รายละเอียด
    if result != expected:
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
        print(f"   Board Input:\n{board}")
        print("-" * 50)

def main():
    print("="*60)
    print("TEST SUITE FOR CHECKMATE")
    print("="*60)

    # --- GROUP 1: Basic Mechanics (พื้นฐาน) ---
    print("\n--- 1. Basic Attacks (R, B, Q, P) ---")
    
    run_test("Rook Horizontal", 
             "R...K\n.....\n.....\n.....\n.....", "Success")
    
    run_test("Rook Vertical", 
             "K....\n.....\n.....\n.....\nR....", "Success")
    
    run_test("Bishop Diagonal", 
             "B....\n.K...\n.....\n.....\n.....", "Success")
    
    run_test("Queen (Rook-like)", 
             "Q...K\n.....\n.....\n.....\n.....", "Success")
    
    run_test("Queen (Bishop-like)", 
             "K....\n.....\n..Q..\n.....\n.....", "Success")

    # Pawn Logic: Pawn อยู่แถวล่าง (kr+1) กินขึ้นไปหา King
    run_test("Pawn Attack (Valid)", 
             ".....\n.K...\nP....\n.....\n.....", "Success")

    # --- GROUP 2: Blocking & Safety (การบังและทางรอด) ---
    print("\n--- 2. Blocking & Safe Scenarios ---")
    
    # มีตัวมาบัง (Pawn บัง Rook) -> ต้อง Fail
    run_test("Blocked by Pawn", 
             "R.P.K\n.....\n.....\n.....\n.....", "Fail")
    
    # มีตัวศัตรูบังกันเอง (Bishop บัง Queen) -> ต้อง Fail (เพราะถือว่าเป็นสิ่งกีดขวางตัวแรก)
    run_test("Blocked by Enemy", 
             "Q.B.K\n.....\n.....\n.....\n.....", "Fail")

    # Pawn อยู่ผิดที่ (เดินถอยหลังไม่ได้) -> ต้อง Fail
    run_test("Pawn Backward (Safe)", 
             "P....\n.K...\n.....\n.....\n.....", "Fail")

    # Pawn อยู่ข้างๆ (กินแนวนอนไม่ได้) -> ต้อง Fail
    run_test("Pawn Side (Safe)", 
             ".PK..\n.....\n.....\n.....\n.....", "Fail")

    # --- GROUP 3: Edge Cases (กรณีขอบเขตและ Input ผิดพลาด) ---
    print("\n--- 3. Edge Cases & Error Handling ---")
    
    # ไม่มี King -> Fail
    run_test("No King", 
             "R....\n.....\n.....\n.....\n.....", "Fail")
    
    # String ว่างเปล่า -> Fail
    run_test("Empty Input", "", "Fail")
    
    # กระดานไม่ใช่จัตุรัส (สี่เหลี่ยมผืนผ้า) -> Fail
    run_test("Rectangle Board", 
             "K...\nR...", "Fail")
    
    # กระดานเบี้ยว (Jagged Array - แถวไม่เท่ากัน) -> Fail
    run_test("Jagged Rows", 
             "R...\n.K\n...", "Fail")

    # กระดานเล็กที่สุดที่ Checkmate ได้ (2x2)
    run_test("2x2 Board Check", 
             "K.\nR.", "Success")

    # กระดาน 1x1 (มีแค่ King)
    run_test("1x1 Board", "K", "Fail")

    # --- GROUP 4: Unregistered Pieces (ตัวอักษรแปลกปลอม) ---
    print("\n--- 4. Garbage & Unregistered Characters ---")
    
    # มีตัวอักษรขยะ 'Z' มาบังทาง -> ต้องมองว่าเป็นกำแพง -> Fail
    run_test("Unknown Char Block (Z)", 
             "R.Z.K\n.....\n.....\n.....\n.....", "Fail")
    
    # มีตัวอักษรขยะ 'X' แต่อยู่ที่อื่น -> ไม่บัง -> Success
    run_test("Unknown Char Ignore", 
             "R...K\n..X..\n.....\n.....\n.....", "Success")

    # ใส่ Emoji มา (ทดสอบ Encoding) -> มองเป็นกำแพง
    run_test("Emoji Block", 
             "R.👻.K\n.....\n.....\n.....\n.....", "Fail")

    print("\n" + "="*60)
    print("Tests Completed.")

if __name__ == "__main__":
    main()
from .game import new_board, place, winner, is_full, ai_move
import sys

def print_board(board):
    print("\n  1 2 3")
    for i, row in enumerate(board, start=1):
        print(f"{i} " + " ".join(row))
    print()

def prompt_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Enter a number.")

def human_turn(board, player):
    while True:
        r = prompt_int(f"{player} move - row (1-3): ") - 1
        c = prompt_int(f"{player} move - col (1-3): ") - 1
        if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == '.':
            if place(board, r, c, player):
                return
        print("Invalid move, try again.")

def main():
    print("=== TIC-TAC-TOE ===")
    print("Mode: (1) Human vs Human  (2) Human vs AI")
    mode = input("> ").strip()
    if mode not in {"1","2"}:
        print("Defaulting to Human vs AI"); mode = "2"

    difficulty = None
    if mode == "2":
        print("Difficulty: (1) Easy  (2) Hard")
        d = input("> ").strip()
        difficulty = "easy" if d == "1" else "hard"
        print(f"AI difficulty: {difficulty}")

    board = new_board()
    current = 'X'
    human = 'X'
    ai = 'O'

    while True:
        print_board(board)
        if winner(board) or is_full(board):
            break

        if mode == "1":
            human_turn(board, current)
        else:
            if current == human:
                human_turn(board, human)
            else:
                r, c = ai_move(board, ai, human, difficulty=difficulty)
                place(board, r, c, ai)
                print(f"AI played at: {r+1} {c+1}")

        current = 'O' if current == 'X' else 'X'

    print_board(board)
    w = winner(board)
    if w:
        print(f"{w} wins!")
    else:
        print("It's a draw.")

if __name__ == "__main__":
    main()

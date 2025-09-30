from typing import List, Optional, Tuple
import math
import random

Board = List[List[str]]  # 'X', 'O', or '.'

def new_board() -> Board:
    return [['.' for _ in range(3)] for _ in range(3)]

def copy_board(board: Board) -> Board:
    return [row[:] for row in board]

def available_moves(board: Board) -> list[Tuple[int,int]]:
    return [(r,c) for r in range(3) for c in range(3) if board[r][c] == '.']

def place(board: Board, r: int, c: int, player: str) -> bool:
    if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == '.':
        board[r][c] = player
        return True
    return False

def winner(board: Board) -> Optional[str]:
    lines = []
    # rows and cols
    for i in range(3):
        lines.append(board[i])  # row
        lines.append([board[0][i], board[1][i], board[2][i]])  # col
    # diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != '.' and line.count(line[0]) == 3:
            return line[0]
    return None

def is_full(board: Board) -> bool:
    return all(cell != '.' for row in board for cell in row)

def game_over(board: Board) -> bool:
    return winner(board) is not None or is_full(board)

def score(board: Board, ai: str) -> int:
    w = winner(board)
    if w == ai:
        return 1
    elif w and w != ai:
        return -1
    return 0

def minimax(board: Board, player: str, ai: str, human: str, alpha: int=-math.inf, beta: int=math.inf) -> Tuple[int, Optional[Tuple[int,int]]]:
    if game_over(board):
        return score(board, ai), None

    best_move = None
    if player == ai:
        best_score = -math.inf
        for (r,c) in available_moves(board):
            board[r][c] = player
            s, _ = minimax(board, human, ai, human, alpha, beta)
            board[r][c] = '.'
            if s > best_score:
                best_score, best_move = s, (r,c)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = math.inf
        for (r,c) in available_moves(board):
            board[r][c] = player
            s, _ = minimax(board, ai, ai, human, alpha, beta)
            board[r][c] = '.'
            if s < best_score:
                best_score, best_move = s, (r,c)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move

def ai_move(board: Board, ai: str, human: str, difficulty: str='hard') -> Tuple[int,int]:
    moves = available_moves(board)
    if not moves:
        raise ValueError("No moves available")
    if difficulty == 'easy':
        return random.choice(moves)
    # hard: minimax
    _, move = minimax(copy_board(board), ai, ai, human)
    return move if move else random.choice(moves)

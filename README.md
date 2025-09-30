# Tic-Tac-Toe (Python, CLI + AI)

A clean, dependency-free Tic-Tac-Toe game you can run in the terminal. Supports **Human vs Human** and **Human vs AI** (random or Minimax).

## Run
```bash
# (optional) python -m venv .venv && source .venv/bin/activate
python -m tictactoe.cli
```

## Features
- 3×3 board with input validation
- Win/draw detection
- Human vs Human
- Human vs AI:
  - **Easy**: random valid moves
  - **Hard**: Minimax (optimal)
- Pure Python, no packages required
- Simple tests (`tests/test_game.py`)

## Project Structure
```
tic-tac-toe/
  tictactoe/
    __init__.py
    game.py  # board + rules
    cli.py   # interactive terminal UX
  tests/
    test_game.py
  README.md
  LICENSE
  .gitignore
```

## Example
```
$ python -m tictactoe.cli
=== TIC-TAC-TOE ===
Mode: (1) Human vs Human  (2) Human vs AI
> 2
Difficulty: (1) Easy  (2) Hard
> 2
You are X. Enter row and column as: 1 1
```

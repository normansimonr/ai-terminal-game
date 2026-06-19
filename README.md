# Norman's Jungle 🐒

A terminal-based jungle adventure where you guide Norman the monkey across a 5×5 grid, collect bananas, and dodge snakes. Built with Python 3 and tested with pytest.

---

## Description

**Norman's Jungle** is a simple but polished text-based game that runs entirely in the terminal. You control **Norman the monkey** (`🐒`) as he explores a jungle grid, grabs **bananas** (`🍌`) to score points, and avoids deadly **snakes** (`🐍`). Every move matters — collect 10 bananas to win, but one wrong step into a snake ends the game.

The project was built iteratively: starting from a basic grid renderer, then layering on WASD movement, collectibles, hazards, a win/lose system, play-again support, and finally a jungle theme.

---

## Features

- **WASD movement** — Navigate the grid with `W` (up), `A` (left), `S` (down), and `D` (right). Boundary checks prevent you from walking off the edge.
- **Collectible scoring** — Walk onto a banana (`🍌`) to collect it. Each banana adds 1 point to your score and respawns at a new random location.
- **Hazard game-over** — Step on a snake (`🐍`) and it's game over immediately.
- **Win condition** — Reach a score of 10 to win. A victory message is displayed and the round ends.
- **Play-again prompt** — After winning or losing, you are asked `Play again? (y/n)`. Answering `y` resets the board and starts a fresh round; `n` exits cleanly.
- **Clear-screen rendering** — The terminal is cleared between turns so the grid always appears in a consistent position.
- **Jungle theme** — Emoji-based graphics (monkey, banana, snake) with a story intro and themed win/lose messages.

---

## How to Run

### Prerequisites

- Python 3.10 or later
- `pytest` (for running tests)

### Launch the game

```bash
python3 game.py
```

Use the **W**, **A**, **S**, **D** keys to move, then press **Enter** after each move.

### Run the tests

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

All tests are located in `test_game.py` and cover movement logic, boundary enforcement, score tracking, target and hazard spawning, reset behaviour, and theme constants.

---

## Gameplay Walkthrough

```
Norman's Jungle 🐒
Explore the jungle, grab bananas, and dodge snakes!

Score: 0
 🐒  ·  ·  ·  · 
 ·  ·  🍌  ·  · 
 ·  ·  ·  ·  · 
 ·  🐍  ·  ·  · 
 ·  ·  ·  ·  · 

Move (W/A/S/D):
```

1. The grid is 5×5. Norman (`🐒`) starts at the top-left corner `(0, 0)`.
2. A banana (`🍌`) and a snake (`🐍`) are placed at random positions each round.
3. Move toward the banana to collect it — your score increases and a new banana spawns.
4. Avoid the snake — stepping on it prints `🐍 A snake got you! Game over!` and ends the round.
5. Collect 10 bananas to see `🎉 You collected all the bananas! Norman conquers the jungle!`

---

## Project Structure

```
.
├── game.py          # Main game logic
├── test_game.py     # Pytest test suite (38 tests)
├── README.md        # This file
└── .gitignore
```

---

## What I Learned

### Iterative Development

This project was built one small feature at a time. Each session added exactly one capability — first the grid, then movement, then a collectible, then scoring, then hazards, then the play-again loop, and finally the theme. This approach made it easy to isolate bugs, because only a handful of lines changed between working states.

### Engineering Prompts to Prevent Regression

Every time I asked for a new feature, I also requested tests for it. Writing tests alongside code caught regressions immediately — for example, when I refactored the game loop to add the play-again prompt, the existing 26 tests confirmed that movement, scoring, and hazards all still worked correctly. The test suite grew from 2 to 38 tests without any test ever needing to be rewritten.

### Using Automated Tests

Automated tests gave me confidence to change the code. I could refactor freely and trust that a simple `pytest` command would tell me if I broke something. Using `pytest.fixture` with `autouse=True` kept each test isolated by resetting global state, which prevented one test's side effects from leaking into another.

### Key Takeaways

- **Start minimal, then layer on.** A working 26-line game loop was easier to extend than a big upfront design.
- **Test the logic, not the visuals.** The tests focus on game rules (movement, scoring, spawning) rather than print output, keeping them fast and stable.
- **Refactor for testability.** Extracting `move_player()`, `check_collection()`, `check_hazard()`, and `reset_game()` into their own functions made the code both cleaner and testable.

---

Built with Python 3, pytest, and a love for terminal games. 🐒🍌🐍

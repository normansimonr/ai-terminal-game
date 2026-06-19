import random

GAME_NAME = "Norman's Jungle \U0001F412"
STORY_INTRO = (
    "Explore the jungle, grab bananas, and dodge snakes!"
)
PLAYER = "\U0001F412"       # 🐒 monkey
COLLECTIBLE = "\U0001F34C"  # 🍌 banana
HAZARD = "\U0001F40D"       # 🐍 snake
WIN_MSG = "\U0001F389 You collected all the bananas! Norman conquers the jungle!"
LOSE_MSG = "\U0001F40D A snake got you! Game over!"

GRID_SIZE = 5
player_x = 0
player_y = 0
score = 0
target_x = 0
target_y = 0
hazard_x = 0
hazard_y = 0


def spawn_target() -> None:
    """Place the target at a random position that is not the player's position."""
    global target_x, target_y
    while True:
        tx = random.randint(0, GRID_SIZE - 1)
        ty = random.randint(0, GRID_SIZE - 1)
        if (tx, ty) != (player_x, player_y):
            target_x, target_y = tx, ty
            break


def spawn_hazard() -> None:
    """Place hazard at a random position not occupied by the player or target."""
    global hazard_x, hazard_y
    while True:
        hx = random.randint(0, GRID_SIZE - 1)
        hy = random.randint(0, GRID_SIZE - 1)
        if (hx, hy) not in ((player_x, player_y), (target_x, target_y)):
            hazard_x, hazard_y = hx, hy
            break


def draw_grid() -> None:
    """Draw the 5x5 grid with the player, target, hazard, and current score."""
    print(f"Score: {score}")
    for row in range(GRID_SIZE):
        line = ""
        for col in range(GRID_SIZE):
            if col == player_x and row == player_y:
                line += f" {PLAYER} "
            elif col == target_x and row == target_y:
                line += f" {COLLECTIBLE} "
            elif col == hazard_x and row == hazard_y:
                line += f" {HAZARD} "
            else:
                line += " \u00B7 "
        print(line)
    print()


def move_player(key: str) -> None:
    """Move the player one step in the given direction, if within bounds."""
    global player_x, player_y
    key = key.lower()
    if key == "w" and player_y > 0:
        player_y -= 1
    elif key == "a" and player_x > 0:
        player_x -= 1
    elif key == "s" and player_y < GRID_SIZE - 1:
        player_y += 1
    elif key == "d" and player_x < GRID_SIZE - 1:
        player_x += 1


def check_collection() -> bool:
    """If the player is on the target, collect it and respawn."""
    global score
    if (player_x, player_y) == (target_x, target_y):
        score += 1
        spawn_target()
        return True
    return False


def check_hazard() -> bool:
    """Return True if the player is on the hazard tile."""
    return (player_x, player_y) == (hazard_x, hazard_y)


def reset_game() -> None:
    """Reset the player, score, and respawn target and hazard."""
    global player_x, player_y, score
    player_x = 0
    player_y = 0
    score = 0
    spawn_target()
    spawn_hazard()


if __name__ == "__main__":
    while True:
        reset_game()
        print(f"\033c{GAME_NAME}")
        print(STORY_INTRO)
        print()
        while True:
            draw_grid()
            move = input("Move (W/A/S/D): ").strip().lower()
            move_player(move)
            if check_hazard():
                print(LOSE_MSG)
                break
            if check_collection() and score >= 10:
                print(WIN_MSG)
                break
            print("\033c", end="")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break

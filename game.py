GRID_SIZE = 5
player_x = 0
player_y = 0


def draw_grid():
    """Draw the 5x5 grid with the player's current position."""
    for row in range(GRID_SIZE):
        line = ""
        for col in range(GRID_SIZE):
            if col == player_x and row == player_y:
                line += " P "
            else:
                line += " . "
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


if __name__ == "__main__":
    while True:
        draw_grid()
        move = input("Move (W/A/S/D): ").strip().lower()
        move_player(move)
        print("\033c", end="")

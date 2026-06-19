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


if __name__ == "__main__":
    while True:
        draw_grid()
        command = input("Enter a command: ").strip().lower()
        print(f"You entered: {command}")

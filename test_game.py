"""Tests for the terminal game."""

import pytest
import game


@pytest.fixture(autouse=True)
def reset_state():
    """Reset the player, score, and target before every test."""
    game.player_x = 0
    game.player_y = 0
    game.score = 0
    game.target_x = 0
    game.target_y = 0
    yield


def test_grid_size():
    """The grid should be 5x5."""
    assert game.GRID_SIZE == 5


def test_player_starts_at_origin():
    """The player should start at position (0, 0)."""
    assert game.player_x == 0
    assert game.player_y == 0


def test_move_right():
    """Moving 'd' increases x by 1."""
    game.move_player("d")
    assert game.player_x == 1
    assert game.player_y == 0


def test_move_left():
    """Moving 'a' decreases x by 1."""
    game.move_player("d")
    game.move_player("d")
    game.move_player("a")
    assert game.player_x == 1
    assert game.player_y == 0


def test_move_down():
    """Moving 's' increases y by 1."""
    game.move_player("s")
    assert game.player_x == 0
    assert game.player_y == 1


def test_move_up():
    """Moving 'w' decreases y by 1."""
    game.move_player("s")
    game.move_player("w")
    assert game.player_x == 0
    assert game.player_y == 0


def test_cannot_move_left_at_left_edge():
    """Player at x=0 should not move left."""
    game.move_player("a")
    assert game.player_x == 0
    assert game.player_y == 0


def test_cannot_move_up_at_top_edge():
    """Player at y=0 should not move up."""
    game.move_player("w")
    assert game.player_x == 0
    assert game.player_y == 0


def test_cannot_move_right_at_right_edge():
    """Player at x=4 should not move right."""
    for _ in range(game.GRID_SIZE - 1):
        game.move_player("d")
    assert game.player_x == game.GRID_SIZE - 1
    game.move_player("d")
    assert game.player_x == game.GRID_SIZE - 1


def test_cannot_move_down_at_bottom_edge():
    """Player at y=4 should not move down."""
    for _ in range(game.GRID_SIZE - 1):
        game.move_player("s")
    assert game.player_y == game.GRID_SIZE - 1
    game.move_player("s")
    assert game.player_y == game.GRID_SIZE - 1


def test_invalid_key_does_nothing():
    """An unrecognised key should not move the player."""
    game.move_player("z")
    assert game.player_x == 0
    assert game.player_y == 0


def test_uppercase_keys_work():
    """Uppercase WASD should work because input is lowercased in the loop."""
    game.move_player("D")
    assert game.player_x == 1
    assert game.player_y == 0


# --- Collectible & scoring tests ---

def test_score_starts_at_zero():
    """Score should start at 0."""
    assert game.score == 0


def test_target_starts_at_origin():
    """Target should initially be at (0, 0)."""
    assert game.target_x == 0
    assert game.target_y == 0


def test_spawn_target_places_within_bounds():
    """spawn_target should place the target inside the grid."""
    game.player_x = 2
    game.player_y = 2
    game.spawn_target()
    assert 0 <= game.target_x < game.GRID_SIZE
    assert 0 <= game.target_y < game.GRID_SIZE


def test_spawn_target_not_on_player():
    """spawn_target should not place the target where the player is."""
    game.player_x = 2
    game.player_y = 2
    for _ in range(50):
        game.spawn_target()
        assert (game.target_x, game.target_y) != (game.player_x, game.player_y)


def test_collection_increments_score():
    """Walking onto the target should increase score by 1."""
    game.target_x = 1
    game.target_y = 0
    game.move_player("d")
    game.check_collection()
    assert game.score == 1


def test_collection_respawns_target():
    """After collecting, the target should move to a new position."""
    game.target_x = 1
    game.target_y = 0
    game.move_player("d")
    game.check_collection()
    assert (game.target_x, game.target_y) != (1, 0)


def test_no_collection_when_not_on_target():
    """Not being on the target should not increase score."""
    game.target_x = 4
    game.target_y = 4
    game.move_player("d")
    game.check_collection()
    assert game.score == 0


def test_collect_all_ten_wins():
    """Score of 10 should end the game with a victory."""
    game.target_x = 1
    game.target_y = 0
    game.player_x = 1
    game.player_y = 0
    for _ in range(9):
        game.check_collection()
        game.player_x = game.target_x
        game.player_y = game.target_y
    game.check_collection()
    assert game.score == 10

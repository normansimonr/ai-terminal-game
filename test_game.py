"""Tests for the terminal game."""

import pytest
import game


@pytest.fixture(autouse=True)
def reset_player():
    """Reset the player to (0, 0) before every test."""
    game.player_x = 0
    game.player_y = 0
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

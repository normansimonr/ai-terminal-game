"""Tests for the terminal game."""

from game import GRID_SIZE, player_x, player_y


def test_grid_size():
    """The grid should be 5x5."""
    assert GRID_SIZE == 5


def test_player_starts_at_origin():
    """The player should start at position (0, 0)."""
    assert player_x == 0
    assert player_y == 0

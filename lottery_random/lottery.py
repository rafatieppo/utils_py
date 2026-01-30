#!/usr/bin/env python3

"""Generate random lottery numbers."""

import random


def app_lottery(games, n, vmin, vmax):
    """
    Generate random lottery numbers.

    Parameters:
    games (int): Number of games/cards to generate.
    n (int): Number of random numbers per game.
    vmin (int): Minimum value for random numbers.
    vmax (int): Maximum value for random numbers.
    
    Returns:
    list: A list of generated games, where each game is a list of unique random numbers.
    """
    if vmax - vmin + 1 < n:
        raise ValueError("The range of values (vmax - vmin) must be at least as large as 'n'.")

    all_games = []
    for i in range(1, games + 1):
        game = sorted(random.sample(range(vmin, vmax + 1), n))  # Ensure unique and sorted numbers
        all_games.append(game)
        print(f"Game {i}: {game}")
    
    print("------------------------------------------------------------")
    return all_games


if __name__ == "__main__":
    try:
        games = int(input("Enter the number of games to generate: "))
        n = int(input("Enter the number of unique numbers per game: "))
        vmin = int(input("Enter the minimum possible value: "))
        vmax = int(input("Enter the maximum possible value: "))

        app_lottery(games, n, vmin, vmax)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

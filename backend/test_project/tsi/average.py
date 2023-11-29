import math
import os
import sys

def average_stats(game_statistics):
    if not game_statistics:
        return {}
    minutes = 0
    points = 0
    assists = 0
    rebounds = 0

    for game in game_statistics:
        minutes += game.get('minutes', 0)
        points += game.get('points', 0)
        assists += game.get('assists', 0)
        rebounds += game.get('rebounds', 0)

    number_of_games = len(game_statistics)
    average_minutes = minutes / number_of_games
    average_points = points / number_of_games
    average_assists = assists / number_of_games
    average_rebounds = rebounds / number_of_games
    
    average_metrics = {
        'average_minutes': average_minutes,
        'average_points': average_points,
        'average_assists': average_assists,
        'average_rebounds': average_rebounds,
    }
    return average_metrics
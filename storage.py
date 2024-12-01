import os
import json
from scraper import FreeToGameAPI

DATA_DIR = "data"


def save_json(filename, data):
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(DATA_DIR, exist_ok=True)
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data saved to {filepath}")
    except IOError as e:
        print(f"Error saving data to {filepath}: {e}")


def store_all_games():
    api = FreeToGameAPI()
    print("Fetching all games...")
    all_games = api.fetch_all_games()
    save_json("all_games.json", all_games)


def store_game_details(game_id):
    api = FreeToGameAPI()
    print(f"Fetching details for game ID {game_id}...")
    game_details = api.fetch_game_details(game_id)
    save_json(f"game_{game_id}.json", game_details)


def store_games_by_platform(platform):
    api = FreeToGameAPI()
    print(f"Fetching games for platform: {platform}...")
    games = api.fetch_games_by_platform(platform)
    save_json(f"games_platform_{platform}.json", games)


def store_games_by_category(category):
    api = FreeToGameAPI()
    print(f"Fetching games for category: {category}...")
    games = api.fetch_games_by_category(category)
    save_json(f"games_category_{category}.json", games)


def store_games_sorted(sort_by):
    api = FreeToGameAPI()
    print(f"Fetching games sorted by: {sort_by}...")
    games = api.fetch_games_sorted(sort_by)
    save_json(f"games_sorted_{sort_by}.json", games)


def store_filtered_games(tags, platform=None):
    api = FreeToGameAPI()
    print(f"Fetching games filtered by tags: {tags} and platform: {platform}...")
    games = api.fetch_games_by_filter(tags, platform)
    tags_str = "_".join(tags)
    filename = f"games_filtered_{tags_str}"
    if platform:
        filename += f"_platform_{platform}"
    filename += ".json"
    save_json(filename, games)


# Call functions to fetch and store data
if __name__ == "__main__":
    store_all_games()
    store_game_details(452)
    store_games_by_platform("pc")
    store_games_by_category("shooter")
    store_games_sorted("release-date")
    store_filtered_games(["mmorpg", "fantasy"], platform="browser")

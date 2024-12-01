import json


def load_games_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return []


def discover_games(genre, platform, sort_by):
    all_games = load_games_from_file("data/all_games.json")

    print(f"Loaded {len(all_games)} games.")  # Debugging: Check number of games loaded

    if genre:
        print(f"Filtering by genre: {genre}")  # Debugging: Log genre being filtered
        all_games = [
            game
            for game in all_games
            if game["genre"].strip().lower() == genre.strip().lower()
        ]
        print(
            f"After filtering by genre '{genre}', {len(all_games)} games found."
        )  # Debugging: Check games remaining after genre filter

    if platform:
        print(
            f"Filtering by platform: {platform}"
        )  # Debugging: Log platform being filtered
        all_games = [
            game for game in all_games if platform.lower() in game["platform"].lower()
        ]
        print(
            f"After filtering by platform '{platform}', {len(all_games)} games found."
        )  # Debugging: Check games remaining after platform filter

    if sort_by == "release-date":
        all_games = sorted(
            all_games, key=lambda x: x.get("release_date", ""), reverse=True
        )
        print(
            "Games sorted by release date."
        )  # Debugging: Confirm sorting by release date

    return all_games

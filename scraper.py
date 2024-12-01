import requests
from bs4 import BeautifulSoup
import json


def scrape_game_data(genre, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    games_data = []

    for game_section in soup.find_all(
        "div", class_="game-card"
    ):  # Adjust class based on actual HTML structure
        game = {}

        # Assuming the game's title, URL, genre, etc., can be scraped from the game-card div
        game["id"] = int(game_section["data-game-id"])
        game["title"] = game_section.find("a", class_="game-title").text.strip()
        game["game_url"] = game_section.find("a", class_="game-title")["href"]
        game["thumbnail"] = game_section.find("img")["src"]
        game["genre"] = genre
        game["platform"] = game_section.find("div", class_="platform").text.strip()
        game["publisher"] = game_section.find("div", class_="publisher").text.strip()
        game["developer"] = game_section.find("div", class_="developer").text.strip()
        game["release_date"] = game_section.find(
            "div", class_="release-date"
        ).text.strip()
        game["short_description"] = game_section.find(
            "p", class_="short-description"
        ).text.strip()

        games_data.append(game)

    return games_data


def scrape_all_game_genres():
    genres = ["Shooter", "MMORPG", "MOBA", "RPG", "Strategy", "Adventure"]
    all_games = []

    for genre in genres:
        # Replace with actual URLs for each genre
        genre_url = f"https://www.freetogame.com/{genre.lower()}-games"
        games = scrape_game_data(genre, genre_url)
        all_games.extend(games)

    return all_games


def save_games_to_file(games, filename):
    with open(filename, "w") as f:
        json.dump(games, f, indent=4)


if __name__ == "__main__":
    all_games = scrape_all_game_genres()
    save_games_to_file(all_games, "data/all_games.json")

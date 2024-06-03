#!/usr/bin/env python3.11

import argparse
import requests


URL = 'https://jsonmock.hackerrank.com/api/tvseries'


def best_in_genre(genre: str) -> str:
    all_series = []
    response = requests.get(URL, timeout=15)
    if response.status_code != 200:
        return 'Error requesting data from api'
    response_json = response.json()
    total_pages = response_json.get('total_pages')
    series = response_json.get('data', [])
    all_series.extend(series)

    for page in range(2, total_pages+1):
        response = requests.get(
            URL,
            params={'page': page},
            timeout=15)
        response_json = response.json()
        series = response_json.get('data', [])
        all_series.extend(series)

    series_by_genre = [
        serie for serie in all_series if genre.lower() in serie.get('genre').lower()
    ]

    if not series_by_genre:
        return f'No series found for genre {genre}'

    sorted_series_by_genre = sorted(series_by_genre,
                                    key=lambda serie: (-serie['imdb_rating'], serie['name']))
    return sorted_series_by_genre[0].get('name', '')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('genre')
    args = parser.parse_args()
    best_serie = best_in_genre(args.genre)
    print(best_serie)


if __name__ == '__main__':
    main()

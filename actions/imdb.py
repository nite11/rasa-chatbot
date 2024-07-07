from bs4 import BeautifulSoup
import requests

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

def fetch_movie_names(release_year_from='1990',release_year_to='2024',user_rating='7'):
    url = f'https://www.imdb.com/search/title/?title_type=feature&release_date={release_year_from}-01-01,{release_year_to}-12-31&user_rating={user_rating},10&genres=!documentary,!short'
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = soup.select('.ipc-title__text')
    list = []

    # Iterating over movies to extract each movie's details
    for index in range(1, 6):
        movie_string = movies[index].get_text()
        movie_string = movie_string[3:]	
        list.append(movie_string)
    return list



movies = [
    {"aty": "1+1", "imdb": 7.0, "category": "Thriller"},
    {"aty": "Hitman", "imdb": 6.3, "category": "Action"},
    {"aty": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"aty": "The Help", "imdb": 8.0, "category": "Drama"},
    {"aty": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"aty": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"aty": "Love", "imdb": 6.0, "category": "Romance"},
    {"aty": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"aty": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"aty": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"aty": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"aty": "What is the aty", "imdb": 9.2, "category": "Suspense"},
    {"aty": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"aty": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"aty": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_highly_rated(movie):
    return movie["imdb"] > 5.5
print(is_highly_rated({"aty": "Hitman", "imdb": 6.3, "category": "Action"}))  
print(is_highly_rated({"aty": "AlphaJet", "imdb": 3.2, "category": "War"}))





def filter_highly_rated(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
print(filter_highly_rated(movies))





def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
print(movies_by_category(movies, "Romance"))





def average_imdb(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)
print(average_imdb(movies))





def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)
print(average_imdb_by_category(movies, "Romance"))
print(average_imdb_by_category(movies, "Thriller"))

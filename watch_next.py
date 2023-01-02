import spacy

nlp = spacy.load('en_core_web_md')

try:
    f = open("movies.txt",'r')
    movies = {}
    for line in f:
        (title,description) = line.split(":")
        movies[title] = description
except FileNotFoundError:
    print("movies.txt does not exist")
except PermissionError:
    print("This program does not have read permissions for movies.txt")
finally:
    f.close()

def watch_next(descr):
    similarities = {}
    for movie in movies:
        if descr not in movies[movie]:
            similarities[movie]=nlp(movies[movie]).similarity(nlp(descr))
    return "You should watch "+max(similarities)+"next."

print(f"example input: {movies['Movie A ']} ")
print(watch_next(movies['Movie A ']))
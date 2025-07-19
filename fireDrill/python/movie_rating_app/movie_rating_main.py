from fireDrill.python.movie_rating_app.Movie_rating_app import menue

movie_list = []

while True:
    menue()
    choice = int(input("Enter your choice: "))
    match choice:
        case "1":
            movie_name = input("enter the movie name: ")
            movie_list.append(movie_name)
            print(f"movie {movie_name} has been added!")

        case "2":



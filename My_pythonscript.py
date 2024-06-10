def print_pizza_toppings(data_structure):
    print("My favourite pizza toppings are:")
    for topping in data_structure["pizza_toppings"]:
        print(f"- {topping}")


def add_pizza_toppings(data_structure, toppings):
    data_structure["pizza_toppings"].extend(toppings)
    data_structure["pizza_toppings"].sort()
    data_structure["pizza_toppings"] = [topping.lower() for topping in data_structure["pizza_toppings"]]



def print_student_info(data_structure):
    full_name =  data_structure["full_name"]
    first_name = full_name.split()[0]
    student_id = data_structure["student_id"]

    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}.")

def print_movie_genre(data_structure):
    genres = [movie["genre"] for movie in data_structure["movies"]]
    genres = list(set(genres)) # Remove duplicates
    genres.sort()

    if len(genres) == 1:
        print(f"I like to watch {genres[0]} movies.")
    else:
        print(f"I like to watch {', '.join(genres[:-1])}, and {genres[-1]} movies.")

def print_movie_titles(movie_list):
    titles = [movie["title"].title() for movie in movie_list]
    if len(titles) == 1:
        print(f"Some of my favourite movies are {titles[0]}!")
    else:
        print(f"Some of my favourite movies are {', '.join(titles[:-1])}, and {titles[-1]}!")

def main():
    data_structure = {
        "full_name": "Mohamed Aadhil",
        "student_id": 10330868,
        "pizza_toppings": ["CHEESE", "OLIVES", "PINEAPPLES"],
        "movies": [
            {"title": "downsizing", "genre": "sci-fi"},
            {"title": "interstellar", "genre": "sci-fi"}
            
        ]
    }
    
    # Print initial pizza toppings
    print_pizza_toppings(data_structure)

    # Add a new movie to the list
    new_movie = {"title": "lovetoday", "genre": "romantic"}
    data_structure["movies"].append(new_movie)
    
    # Add new pizza toppings
    new_toppings = ("MUSHROOMS","ONIONS","BACON")
    add_pizza_toppings(data_structure, new_toppings)

    # print updated pizza toppings
    print_pizza_toppings(data_structure)
    
    print_student_info(data_structure)

    print_movie_genre(data_structure)

    print_movie_titles(data_structure["movies"])

if __name__ == '__main__':
    main()
